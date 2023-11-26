from django.db import models
from vendor.models import Vendor

# Create your models here.

class PurchaseOrder:
    po_number = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField()
    issue_date = models.DateField()
    acknowledgment_date = models.DateField()
    