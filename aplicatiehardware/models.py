from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db.models.functions import Length

# Entitatea Categorie
class Categorie(models.Model):
    nume = models.CharField(
        max_length=100, 
        unique=True, # [5%] va exista minim un câmp unic
        error_messages={ # [10%] definiți în minim 5 câmpuri mesaje de eroare
            'unique': "O categorie cu acest nume există deja.",
            'max_length': "Numele categoriei este prea lung."
        }
    )
    descriere = models.TextField(
        null=True, # [5%] vor exista minim 5 câmpuri care admit și valori de tip null (1/5)
        blank=True
    )
    culoare_stilizare = models.CharField(max_length=50, default="#FFFFFF")
    sigla = models.ImageField( # [5%] Să aveți minim un câmp de tip ImageField sau FileField
        upload_to='categorii_sigle/', 
        null=True, # (2/5)
        blank=True
    )
    
    class Dificultate(models.TextChoices): # [10%] va exista minim un câmp cu choices
        USOR = 'usor', 'Usor'
        MEDIU = 'mediu', 'Mediu'
        AVANSAT = 'avansat', 'Avansat'
        EXPERT = 'expert', 'Expert'

    nivel_dificultate = models.CharField(
        max_length=20,
        choices=Dificultate.choices,
        default=Dificultate.MEDIU # [10%] vor exista minim 4 câmpuri cu valoare default (1/4)
    )

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categorii"
        ordering = ['nume'] # [5%] pentru minim 2 modele stabiliți ordonarea implicită (1/2)

    def __str__(self):
        return self.nume

# Entitatea Brand
class Brand(models.Model):
    nume = models.CharField(max_length=100, unique=True)
    tara_origine = models.CharField(max_length=100)
    website = models.URLField( # [5%] va exista minim un câmp care are tipul ales dintre EmailField, URLField, SlugField
        null=True, # (3/5)
        blank=True,
        help_text="Introduceți adresa completă a site-ului web (ex: https://www.exemplu.com)" # [5%] minim 5 câmpuri vor avea definit help_text (1/5)
    )

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Branduri"

    def __str__(self):
        return self.nume

# Entitatea Furnizor
class Furnizor(models.Model):
    nume_companie = models.CharField(max_length=150, unique=True)
    email_contact = models.EmailField(
        unique=True,
        help_text="Adresa de email oficială pentru achiziții B2B.", # (2/5)
        error_messages={ # [10%] definiți în minim 5 câmpuri mesaje de eroare
            'unique': "Există deja un furnizor cu acest email."
        }
    )
    telefon = models.CharField(
        max_length=20, 
        null=True, # (4/5)
        blank=True
    )
    
    class Meta:
        verbose_name = "Furnizor"
        verbose_name_plural = "Furnizori"

    def __str__(self):
        return self.nume_companie

# Entitatea Componenta (Produsul)
class Componenta(models.Model):
    nume = models.CharField(
        max_length=200, 
        unique=True,
        error_messages={ # [10%] definiți în minim 5 câmpuri mesaje de eroare
            'unique': "Numele componentei trebuie să fie unic."
        }
    )
    pret = models.FloatField(
        help_text="Prețul unitar exprimat în LEI.", # (3/5)
        error_messages={ # [10%] definiți în minim 5 câmpuri mesaje de eroare
            'invalid': "Vă rugăm să introduceți o valoare numerică validă pentru preț."
        }
    )
    in_stoc = models.BooleanField(
        default=True, # [10%] vor exista minim 4 câmpuri cu valoare default (2/4)
        help_text="Bifați dacă produsul este disponibil în depozit." # (4/5)
    )
    data_aparitie = models.DateField(
        null=True, # (5/5) - Cerință atinsă
        blank=True
    )
    data_adaugare = models.DateTimeField(
        auto_now_add=True, # [5%] va exista minim un câmp de tip datetime, care are ca valoare imiplicită data adăugării
        help_text="Data și ora la care produsul a fost adăugat în sistem." # (5/5) - Cerință atinsă
    )
    
    class StareProdus(models.TextChoices):
        NOU = 'nou', 'Nou'
        RESIGILAT = 'resigilat', 'Resigilat'
        SH = 'sh', 'Second-Hand'

    stare = models.CharField(
        max_length=20,
        choices=StareProdus.choices,
        default=StareProdus.NOU # [10%] vor exista minim 4 câmpuri cu valoare default (3/4)
    )
    
    # Atribut vector cerut in cerinte
    porturi_interfata = ArrayField(
        models.CharField(max_length=50, blank=True),
        default=list, # [10%] vor exista minim 4 câmpuri cu valoare default (4/4) - Cerinta atinsa. Admite loc liber.
        blank=True,
        null=True
    )

    # Relații
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="componente")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="componente")
    furnizori = models.ManyToManyField(Furnizor, related_name="componente_livrate") # Relatie M:N

    class Meta:
        verbose_name = "Componentă"
        verbose_name_plural = "Componente"
        ordering = ['-data_adaugare'] # [5%] pentru minim 2 modele stabiliți ordonarea implicită (2/2) - Cerință atinsă
        indexes = [ # [10%] alegeți minim 4 câmpuri care ar avea sens să fie indexate
            models.Index(fields=['nume'], name='nume_comp_idx'),
            models.Index(fields=['pret'], name='pret_comp_idx'),
            models.Index(fields=['in_stoc'], name='stoc_comp_idx'),
            models.Index(fields=['stare'], name='stare_comp_idx'),
        ]
        constraints = [ # [25%] definiți minim 5 constrângeri folosind models.Q
            models.CheckConstraint(
                condition=models.Q(pret__gt=0),
                name='pret_pozitiv_componenta',
                violation_error_message="Prețul componentei trebuie să fie strict pozitiv!"
            ),
            models.CheckConstraint(
                condition=models.Q(nume__iregex=r'^.{3,}$'),#verifica iregex daca are minimum 3 caractere
                name='nume_lungime_minima',
                violation_error_message="Numele componentei trebuie să aibă cel puțin 3 caractere."
    )
        ]

    def __str__(self):
        return f"{self.nume} ({self.stare})"

# Entitatea Specificatie_Tehnica (Entitate Slaba)
class SpecificatieTehnica(models.Model):
    componenta = models.ForeignKey(Componenta, on_delete=models.CASCADE, related_name="specificatii")
    nume_spec = models.CharField(max_length=100)
    valoare = models.CharField(
        max_length=150,
        error_messages={ # [10%] definiți în minim 5 câmpuri mesaje de eroare (5/5) - Cerință atinsă
            'max_length': "Valoarea specificației este prea lungă."
        }
    )

    class Meta:
        verbose_name = "Specificație Tehnică"
        verbose_name_plural = "Specificații Tehnice"
        constraints = [ # Continuare constrangeri (total 5 necesare)
            models.UniqueConstraint( # Aceasta actioneaza ca si cheie partiala (identificare)
                fields=['componenta', 'nume_spec'],
                name='unique_spec_pe_componenta',
                violation_error_message="O componentă nu poate avea două specificații cu același nume."
            ),
            models.CheckConstraint(
                condition=~models.Q(valoare=""),
                name='valoare_spec_nu_e_goala',
                violation_error_message="Valoarea specificației nu poate fi goală."
            ),
             models.CheckConstraint(
                condition=~models.Q(nume_spec=""),
                name='nume_spec_nu_e_gol',
                violation_error_message="Numele specificației nu poate fi gol."
            )
        ]

    def __str__(self):
        return f"{self.componenta.nume} - {self.nume_spec}: {self.valoare}"