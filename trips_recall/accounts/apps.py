from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trips_recall.accounts'

    def ready(self):
        import trips_recall.accounts.signals
