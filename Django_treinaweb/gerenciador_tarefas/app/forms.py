from django import forms
from .models import Tarefas

# A validação dos dados do formulario ocorre conforme as configurações definidas no models.Tarefas


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = '__all__'
