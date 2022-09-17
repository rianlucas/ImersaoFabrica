from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'categoria']

field_titulo = TaskForm.base_fields['titulo']
field_titulo.widget.attrs['class'] = 'special'