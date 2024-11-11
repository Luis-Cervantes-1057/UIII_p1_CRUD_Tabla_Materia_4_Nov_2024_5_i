from django.urls import path
from materia_app import views

urlpatterns = [
    path("", views.inicio_vistas, name="inicio_vistas"),
    path("registrarMateria/", views.registrarMateria, name="registrarMateria"),
    
    path("borrarMateria/<codigo>", views.borrarMateria, name="borrarMateria"),
    path("seleccionarMateria/<codigo>", views.seleccionarMateria, name="seleccionarMateria"),
    path("editarMateria/<codigo>", views.editarMateria, name="editarMateria")
]
