from django import forms
from WarframePracticaApp.models import WarframeCampos

class WarframeForm(forms.ModelForm):
    class Meta:
        model = WarframeCampos
        fields = '__all__'