from django import forms
from .models import personas

class PersonaFrom(forms.ModelForm):
    class Meta:
        model = personas
        fields = '__all__'
        