from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_wa = models.CharField(max_length=100, null=True, default='00000')
    imageProfil = models.ImageField(null=True, blank=True, upload_to="images/")