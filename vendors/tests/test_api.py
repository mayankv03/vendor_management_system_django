from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from vendors.models import Vendor, PurchaseOrder
from datetime import datetime

class VendorAPITest(APITestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Mayank Test",
            contact_details="9876543210",
            address="MP Nagar, Bhopal",
            vendor_code="MYNK003"
        )
        self.vendor_url = reverse('vendor-list')

    def test_create_vendor(self):
        data = {
            "name": "Mayank Vishwakarma",
            "contact_details": "0987654321",
            "address": "MP Nagar, Zone 1, Bhopal",
            "vendor_code": "MYNKV03"
        }
        response = self.client.post(self.vendor_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_list_vendors(self):
        response = self.client.get(self.vendor_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class PurchaseOrderAPITest(APITestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Mayank Test",
            contact_details="9876543210",
            address="MP Nagar, Bhopal",
            vendor_code="MYNK003"
        )
        self.po_url = reverse('purchaseorder-list')
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=datetime.now(),
            delivery_date=datetime.now(),
            items={"item": "Test Item", "quantity": 5},
            quantity=5,
            status="pending",
            issue_date=datetime.now()
        )

    def test_create_purchase_order(self):
        data = {
            "po_number": "PO002",
            "vendor": self.vendor.id,
            "order_date": datetime.now(),
            "delivery_date": datetime.now(),
            "items": {"item": "New Item", "quantity": 20},
            "quantity": 20,
            "status": "pending",
            "issue_date": datetime.now()
        }
        response = self.client.post(self.po_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)

    def test_list_purchase_orders(self):
        response = self.client.get(self.po_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
