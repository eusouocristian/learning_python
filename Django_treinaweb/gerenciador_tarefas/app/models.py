from django.db import models

# Create your models here.
# Após criar o modelo (criação das tarefas de comunicação com o banco de dados)
# é preciso executar >>> python manage.py makemigrations
# Para aplicar a criação dos campos no banco de dados conforme a migração criada,
# é preciso executar >>> python manage.py migrate

class Tarefas(models.Model):
    PRIORIDADE_CHOICES = [
        ('A', 'Alta'),
        ('N', 'Normal'),
        ('B', 'Baixa')
    ]

    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)

