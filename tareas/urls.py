"""gestion_tareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Ruta para la página principal donde se listan las tareas
    path('', views.lista_tareas, name='lista_tareas'),
    
    # Ruta para crear una nueva tarea
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    
    # Ruta para editar una tarea
    path('tareas/editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    
    # Ruta para eliminar una tarea
    path('tareas/eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    
]