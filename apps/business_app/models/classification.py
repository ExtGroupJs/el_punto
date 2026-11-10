from django.db import models


class Classification(models.Model):
    name = models.CharField(verbose_name="Nombre", unique=True, max_length=100)
    extra_info = models.TextField(verbose_name="Información adicional", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Clasificación"
        verbose_name_plural = "Clasificaciones"

    def __str__(self):
        return self.name
