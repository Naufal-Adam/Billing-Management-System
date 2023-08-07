from django.db import models

# Create your models here.
class client(models.Model):
    nama_client = models.CharField(max_length=100, null=True)
    no_wa_client = models.CharField(max_length=100, null=True)
    email_client = models.CharField(max_length=100, null=True)
    kode_pos = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nama_client} {self.no_wa_client} {self.email_client} {self.kode_pos}"
    
class clientAlamat(models.Model):
    client = models.OneToOneField(client, on_delete=models.CASCADE, null=True)
    jalan = models.CharField(max_length=100, null=True)
    kabupaten = models.CharField(max_length=100, null=True)
    provinsi = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.jalan} {self.kabupaten} {self.provinsi}"