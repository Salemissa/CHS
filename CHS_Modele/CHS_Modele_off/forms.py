from django import forms
from .models import CHSModel

class CHSModelForm(forms.ModelForm):
    class Meta:
        model = CHSModel
        exclude = ['score', 'decision', 'num_dossier']