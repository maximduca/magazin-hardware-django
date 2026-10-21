from django.contrib import admin
from .models import Categorie, Brand, Furnizor, Componenta, SpecificatieTehnica

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nume', 'nivel_dificultate')
    search_fields = ('nume',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('nume', 'tara_origine', 'website')
    search_fields = ('nume', 'tara_origine')

@admin.register(Furnizor)
class FurnizorAdmin(admin.ModelAdmin):
    list_display = ('nume_companie', 'email_contact', 'telefon')
    search_fields = ('nume_companie', 'email_contact')

@admin.register(Componenta)
class ComponentaAdmin(admin.ModelAdmin):
    list_display = ('nume', 'categorie', 'brand', 'pret', 'in_stoc', 'stare', 'data_adaugare')
    list_filter = ('in_stoc', 'stare', 'categorie', 'brand')
    search_fields = ('nume',)

@admin.register(SpecificatieTehnica)
class SpecificatieTehnicaAdmin(admin.ModelAdmin):
    list_display = ('componenta', 'nume_spec', 'valoare')
    list_filter = ('nume_spec',)
    search_fields = ('componenta__nume', 'nume_spec')