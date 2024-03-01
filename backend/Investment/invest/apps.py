from django.apps import AppConfig


class InvestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "invest"

    #calls the signal that creates a wallet when a user signsup
    def ready(self):
        import invest.signals  # Import your signals file
