from django.urls import path

from Miproyectito.views import mostrar_familia, include
urlpatterns = [
    path("familia/", mostrar_familia)
    
]