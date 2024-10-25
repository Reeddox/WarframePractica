from django import forms
from django.core.exceptions import ValidationError
from WarframePracticaApp.models import WarframeCampos

class WarframeForm(forms.ModelForm):
    class Meta:
        model = WarframeCampos
        fields = '__all__'
        
    def clean_CriticalUtility(self):
        critical_utility = self.cleaned_data.get('CriticalUtility')
        if critical_utility < 0:
            raise forms.ValidationError("Critical Utility no puede ser menor a 0")
        elif critical_utility > 50:
            raise forms.ValidationError("Critical Utility no puede ser mayor a 50")
        
        CalculoCritical_Utility = critical_utility / 100
        
        return CalculoCritical_Utility

    def clean_CriticalDMG(self):
        critical_dmg = self.cleaned_data.get('CriticalDMG')
        if critical_dmg < 1:
            raise forms.ValidationError("CriticalDMG no puede ser menor a 1")
        elif critical_dmg > 5:
            raise forms.ValidationError("CriticalDMG no puede ser mayor a 5")
        return critical_dmg

    def clean_StatusUtility(self):
        status_utility = self.cleaned_data.get('StatusUtility')
        if status_utility < 0:
            raise forms.ValidationError("Critical Utility no puede ser menor a 0")
        elif status_utility > 50:
            raise forms.ValidationError("Status Utility no puede ser mayor a 50")
        
        CalculoStatus_Utility = status_utility / 100
        
        return CalculoStatus_Utility
    
    def clean(self):
        cleaned_data = super().clean()
        warframe_nombre = self.cleaned_data.get('WarframeNombre')
        critical_utility = self.cleaned_data.get('CriticalUtility')
        critical_dmg = self.cleaned_data.get('CriticalDMG')
        status_utility = self.cleaned_data.get('StatusUtility')
        
        if warframe_nombre is None or critical_utility is None or critical_dmg is None or status_utility is None:
            raise forms.ValidationError("Todos los campos son obligatorios")
        
        return cleaned_data