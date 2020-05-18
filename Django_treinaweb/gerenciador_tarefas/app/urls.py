from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # caminho listar_tarefas/ vai executar o metodo listar_tarefas do arquivo views.py
    # a rota possui um nome 'listar_tarefas'
    path("listar_tarefas/", listar_tarefas, name='listar_tarefas'),
]
