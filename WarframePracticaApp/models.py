from django.db import models

# Create your models here.
class WarframeCampos(models.Model):
    WarframeNombre = models.CharField(max_length = 50)
    CriticalUtility = models.FloatField()
    CriticalDMG = models.FloatField()
    StatusUtility = models.FloatField()