from django.db import models

class datos(models.Model):
    texto = models.CharField(max_length=100, verbose_name="Texto")
    descripción = models.CharField(blank=True, max_length=200, verbose_name="Descripción")

