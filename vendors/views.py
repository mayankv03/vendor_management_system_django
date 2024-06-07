from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(performance_data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
        metrics = vendor.calculate_performance_metrics()
        return Response(metrics, status=status.HTTP_200_OK)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        return Response({"message": "Acknowledgment updated"}, status=status.HTTP_200_OK)
    except PurchaseOrder.DoesNotExist:
        return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
