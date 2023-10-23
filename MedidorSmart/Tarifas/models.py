from django.db import models

# Create your models here.
class TarifaLuz(models.Model):
    TIPOS_CHOICES = (
        ('1A', '1A'),
        ('1B', '1B'),
        ('1C', '1C'),
        ('1E', '1E'),
        ('1F', '1F'),
        ('DAC', 'DAC'),
    )

    tipo = models.CharField(max_length=3, choices=TIPOS_CHOICES)
    ano = models.IntegerField()
    mes = models.CharField(max_length=10)
    consumo_basico = models.DecimalField(max_digits=10, decimal_places=3)
    consumo_intermedio = models.DecimalField(max_digits=10, decimal_places=3)
    consumo_excedente = models.DecimalField(max_digits=10, decimal_places=3)
