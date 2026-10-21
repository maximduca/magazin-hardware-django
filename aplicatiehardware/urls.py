from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index', views.index, name="index"), 
    path('info', views.info, name="info"),
    path('despre', views.despre, name="despre"),
    path('istoric', views.istoric, name="istoric"),
    path('log', views.pagina_log, name="log"),
    path('produse', views.produse, name="produse"),
    path('contact', views.contact, name="contact"),

    re_path(r'^accesare(?P<id>\d+)$', views.afisare_accesare, name="afisare_accesare"),
]