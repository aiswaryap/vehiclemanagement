from . models import vehicle
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=vehicle
        fields=['number','type','model','description']