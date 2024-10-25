from django.contrib import admin
from WarframePracticaApp.models import WarframeCampos

# Register your models here.

class WarframeAdmin(admin.ModelAdmin):
    list_display = ['WarframeNombre', 'CriticalUtility', 'CriticalDMG', 'StatusUtility']

admin.site.register(WarframeCampos)
