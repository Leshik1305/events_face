from django.db import models


class SyncResult(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    new_events_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество новый мероприятий"
    )
    updated_events_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество обновленных мероприятий"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Синхронизация"
        verbose_name_plural = "Синхронизации"
