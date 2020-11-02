from django.db import models

class TestLocation(models.Model):
    name = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    phone_number = models.CharField(max_length=500, null=True)
    website = models.CharField(max_length=500, null=True)
    active = models.BooleanField(default=True)