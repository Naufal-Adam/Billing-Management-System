from django.db import models
from clients.models import client
from products.models import produk

# Create your models here.
class invoice(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    produk = models.ForeignKey(produk, on_delete=models.CASCADE, null=True)
    no_invoice = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    subtotal = models.IntegerField()
    total = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.no_invoice} {self.item} {self.quantity} {self.price} {self.subtotal} {self.total} {self.date}"