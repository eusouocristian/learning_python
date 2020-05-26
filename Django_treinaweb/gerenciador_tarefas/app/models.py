from django.db import models
from django.contrib.auth.models import User
# Models é reponsável pela criação da estrutura de tabela do banco de dados
# As tarefas de registros no banco de dados são feitas pela camada services (app/services/tarefa_service)

# Após criar o modelo (criação das tarefas de comunicação com o banco de dados)
# é preciso executar >>> python manage.py makemigrations
# Para aplicar a criação dos campos no banco de dados conforme a migração criada,
# é preciso executar >>> python manage.py migrate


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("A", "Alta"),
        ("N", "Normal"),
        ("B", "Baixa")
    ]

    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
