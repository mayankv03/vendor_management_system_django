from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    # Logic to update vendor metrics
    pass
