from django.urls import path
from app.views.tarefa_views import *
from app.views.usuario_views import *

urlpatterns = [
    # caminho listar_tarefas/ vai executar o metodo listar_tarefas do arquivo tarefa_views.py
    # a rota possui um nome 'listar_tarefas'
    path("", listar_tarefas, name='listar_tarefas'),
    path("listar_tarefas/", listar_tarefas, name='listar_tarefas'),
    path("cadastrar_tarefa/", cadastrar_tarefa, name='cadastrar_tarefa'),
    path("editar_tarefa/<int:id>", editar_tarefa, name='editar_tarefa'),
    path("remover_tarefa/<int:id>", remover_tarefa, name='remover_tarefa'),
    path("cadastrar_usuario/", cadastrar_usuario, name='cadastrar_usuario'),
    path("logar_usuario/", logar_usuario, name='logar_usuario'),
    path("deslogar_usuario/", deslogar_usuario, name='deslogar_usuario'),

]
