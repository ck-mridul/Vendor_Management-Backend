from django.db import models

# Create your models here.

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address  = models.TextField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate  = models.FloatField()
    

class VendorPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
