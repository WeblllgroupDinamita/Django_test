from django import forms
from .models import datos

class DatoForm(forms.ModelForm):

    class Meta:
            model = datos
            fields = '__all__'