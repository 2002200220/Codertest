from django.urls import path

from Miproyectito.views import mostrar_familia

urlpatterns = [
    path("", mostrar_familia)
    
]