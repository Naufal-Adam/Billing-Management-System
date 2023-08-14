from django.db import models
from clients.models import client
from products.models import produk

# Create your models here.
class invoice(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    no_invoice = models.CharField(max_length=100, null=True)
    invoice_date = models.DateField(null=True)
    invoice_due_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.no_invoice} {self.invoice_date} {self.invoice_due_date}"

class invoiceProduk(models.Model):
    produk = models.ForeignKey(produk, on_delete=models.CASCADE, null=True)
    proinvoice = models.ForeignKey(invoice, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.item} {self.quantity} {self.price}"