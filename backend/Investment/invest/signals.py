from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        # Import the Wallet model
        from .models import Wallet

        # Default values for the wallet
        default_bonus = 100  # Example default bonus value
        default_invested = 0  # Example default invested value

        # Create the wallet instance
        Wallet.objects.create(user=instance, bonus=default_bonus, invested=default_invested)
