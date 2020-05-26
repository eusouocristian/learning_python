from django import forms
from .models import Tarefa

# A validação dos dados do formulario ocorre conforme as configurações definidas no models.Tarefas


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        # formulario pode ser submetido sem o campo 'usuario'
        exclude = ('usuario', )
        fields = '__all__'
