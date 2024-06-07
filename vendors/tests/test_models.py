from django.test import TestCase
from vendors.models import Vendor, PurchaseOrder
from datetime import datetime

class VendorModelTest(TestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Mayank Test",
            contact_details="9876543210",
            address="MP Nagar, Bhopal",
            vendor_code="MYNK003"
        )

    def test_vendor_creation(self):
        self.assertEqual(self.vendor.name, "Mayank Test")
        self.assertEqual(self.vendor.vendor_code, "MYNK003")

class PurchaseOrderModelTest(TestCase):

    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Mayank Test",
            contact_details="9876543210",
            address="MP Nagar, Bhopal",
            vendor_code="MYNK003"
        )
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=datetime.now(),
            delivery_date=datetime.now(),
            items={"item": "Test Item", "quantity": 10},
            quantity=10,
            status="pending",
            issue_date=datetime.now()
        )

    def test_purchase_order_creation(self):
        self.assertEqual(self.purchase_order.po_number, "PO001")
        self.assertEqual(self.purchase_order.vendor.name, "Mayank Test")
