from django.db import models
from django.db import models
from clients.models import client
from products.models import produk

# Create your models here.
class setting(models.Model):
    date_notif = models.DateField(null=True)
    time_notif = models.TimeField(null=True)
    text_notif = models.TextField(null=True)
    to_who = models.CharField(null=True, max_length=100)
    to_sms = models.CharField(null=True, max_length=100)
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    produk = models.ForeignKey(produk, on_delete=models.CASCADE, null=True)