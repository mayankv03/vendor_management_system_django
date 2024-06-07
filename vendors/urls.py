from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet, vendor_performance, acknowledge_purchase_order
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order, name='acknowledge-purchase-order'),
]
