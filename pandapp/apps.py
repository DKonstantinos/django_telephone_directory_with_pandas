from django.apps import AppConfig


class PandappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pandapp'

    def ready(self):
        import pandapp.signals
