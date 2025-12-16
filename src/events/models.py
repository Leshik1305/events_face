import uuid

from django.db import models


class Place(models.Model):
    """Модель места проведения мероприятия"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID площадки",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название площадки",
    )

    class Meta:
        ordering = ["-name"]
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"

    def __str__(self):
        return self.name


class EventStatus(models.TextChoices):
    OPEN = "open", "Open"
    CLOSED = "closed", "Closed"


class Event(models.Model):
    """Модель мероприятия"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID мероприятия",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название мероприятия",
    )
    date = models.DateField(verbose_name="Дата проведения")
    status = models.CharField(
        max_length=6,
        choices=EventStatus.choices,
        default=EventStatus.OPEN,
        verbose_name="Статус мероприятия",
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="events",
        verbose_name="Место проведения",
    )

    class Meta:
        ordering = ["-date", "name"]
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return f"Название: {self.name}. Дата проведения: {self.date}. Статус - {self.status}"
