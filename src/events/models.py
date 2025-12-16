from uuid import uuid4

from django.db import models

class Place(models.Model):
    """Модель места проведения событий"""
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False, verbose_name="ID площадки")
    name = models.CharField(max_length=255, verbose_name="Название площадки")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-name']
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'


