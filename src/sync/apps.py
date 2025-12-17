from django.apps import AppConfig


class SyncConfig(AppConfig):
    name = "sync"
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Синхронизация"
