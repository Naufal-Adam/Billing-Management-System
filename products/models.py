from django.db import models
from django.db import models
from clients.models import client

# Create your models here.
class produk(models.Model):
    nama_produk = models.CharField(max_length=100, null=True)
    type_produk = models.CharField(max_length=100, null=True)
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.nama_produk}"