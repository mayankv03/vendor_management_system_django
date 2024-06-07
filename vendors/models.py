from django.db import models, transaction
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(max_length=255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=100)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def calculate_performance_metrics(self):
        purchase_orders = PurchaseOrder.objects.filter(vendor=self)

        # Calculate on_time_delivery_rate
        on_time_deliveries = purchase_orders.filter(status='completed', delivery_date__lte=models.F('order_date'))
        on_time_delivery_rate = (on_time_deliveries.count() / purchase_orders.count()) * 100 if purchase_orders.exists() else 0

        # Calculate quality_rating_avg
        quality_rating_avg = purchase_orders.aggregate(models.Avg('quality_rating'))['quality_rating__avg'] or 0

        # Calculate average_response_time
        acknowledged_orders = purchase_orders.filter(acknowledgment_date__isnull=False)
        response_times = [
            (po.acknowledgment_date - po.order_date).total_seconds()
            for po in acknowledged_orders
        ]
        average_response_time = sum(response_times) / len(response_times) if response_times else 0

        # Calculate fulfillment_rate
        fulfilled_orders = purchase_orders.filter(status='completed')
        fulfillment_rate = (fulfilled_orders.count() / purchase_orders.count()) * 100 if purchase_orders.exists() else 0

        return {
            "on_time_delivery_rate": on_time_delivery_rate,
            "quality_rating_avg": quality_rating_avg,
            "average_response_time": average_response_time,
            "fulfillment_rate": fulfillment_rate,
        }

    @transaction.atomic
    def update_performance_metrics(self):
        metrics = self.calculate_performance_metrics()
        self.on_time_delivery_rate = metrics['on_time_delivery_rate']
        self.quality_rating_avg = metrics['quality_rating_avg']
        self.average_response_time = metrics['average_response_time']
        self.fulfillment_rate = metrics['fulfillment_rate']
        self.save()

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('completed', 'Completed')])
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()