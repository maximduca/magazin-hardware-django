from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db.models.functions import Length

# Entitatea Categorie
class Categorie(models.Model):
    nume = models.CharField(
        max_length=100, 
        unique=True, 
        error_messages={ 
            'unique': "O categorie cu acest nume există deja.",
            'max_length': "Numele categoriei este prea lung."
        }
    )
    descriere = models.TextField(
        null=True, 
        blank=True
    )
    culoare_stilizare = models.CharField(max_length=50, default="#FFFFFF")
    sigla = models.ImageField( 
        upload_to='categorii_sigle/', 
        null=True, 
        blank=True
    )
    
    class Dificultate(models.TextChoices): 
        USOR = 'usor', 'Usor'
        MEDIU = 'mediu', 'Mediu'
        AVANSAT = 'avansat', 'Avansat'
        EXPERT = 'expert', 'Expert'

    nivel_dificultate = models.CharField(
        max_length=20,
        choices=Dificultate.choices,
        default=Dificultate.MEDIU 
    )

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categorii"
        ordering = ['nume']

    def __str__(self):
        return self.nume

# Entitatea Brand
class Brand(models.Model):
    nume = models.CharField(max_length=100, unique=True)
    tara_origine = models.CharField(max_length=100)
    website = models.URLField(
        null=True, 
        blank=True,
        help_text="Introduceți adresa completă a site-ului web"
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
        help_text="Adresa de email oficială pentru achiziții B2B.", 
        error_messages={
            'unique': "Există deja un furnizor cu acest email."
        }
    )
    telefon = models.CharField(
        max_length=20, 
        null=True,
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
        error_messages={
            'unique': "Numele componentei trebuie să fie unic."
        }
    )
    pret = models.FloatField(
        help_text="Prețul unitar exprimat în LEI.", 
        error_messages={
            'invalid': "Vă rugăm să introduceți o valoare numerică validă pentru preț."
        }
    )
    in_stoc = models.BooleanField(
        default=True,
        help_text="Bifați dacă produsul este disponibil în depozit." # 
    )
    data_aparitie = models.DateField(
        null=True, 
        blank=True
    )
    data_adaugare = models.DateTimeField(
        auto_now_add=True,
        help_text="Data și ora la care produsul a fost adăugat în sistem." 
    )
    
    class StareProdus(models.TextChoices):
        NOU = 'nou', 'Nou'
        RESIGILAT = 'resigilat', 'Resigilat'
        SH = 'sh', 'Second-Hand'

    stare = models.CharField(
        max_length=20,
        choices=StareProdus.choices,
        default=StareProdus.NOU 
    )
    
    porturi_interfata = ArrayField(
        models.CharField(max_length=50, blank=True),
        default=list,
        blank=True,
        null=True
    )


    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="componente")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="componente")
    furnizori = models.ManyToManyField(Furnizor, related_name="componente_livrate") # Relatie M:N

    class Meta:
        verbose_name = "Componentă"
        verbose_name_plural = "Componente"
        ordering = ['-data_adaugare']
        indexes = [ 
            models.Index(fields=['nume'], name='nume_comp_idx'),
            models.Index(fields=['pret'], name='pret_comp_idx'),
            models.Index(fields=['in_stoc'], name='stoc_comp_idx'),
            models.Index(fields=['stare'], name='stare_comp_idx'),
        ]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(pret__gt=0),
                name='pret_pozitiv_componenta',
                violation_error_message="Prețul componentei trebuie să fie strict pozitiv!"
            ),
            models.CheckConstraint(
                condition=models.Q(nume__iregex=r'^.{3,}$'),
                name='nume_lungime_minima',
                violation_error_message="Numele componentei trebuie să aibă cel puțin 3 caractere."
    )
        ]

    def __str__(self):
        return f"{self.nume} ({self.stare})"

# Entitatea SpecificatieTehnica (Entitate Slaba)
class SpecificatieTehnica(models.Model):
    componenta = models.ForeignKey(Componenta, on_delete=models.CASCADE, related_name="specificatii")
    nume_spec = models.CharField(max_length=100)
    valoare = models.CharField(
        max_length=150,
        error_messages={ 
            'max_length': "Valoarea specificației este prea lungă."
        }
    )

    class Meta:
        verbose_name = "Specificație Tehnică"
        verbose_name_plural = "Specificații Tehnice"
        constraints = [
            models.UniqueConstraint( 
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