from django import forms
from .models import Tarea  # Asegúrate de que tu modelo Tarea esté correctamente importado

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']  # Reemplaza estos campos según tu modelo
