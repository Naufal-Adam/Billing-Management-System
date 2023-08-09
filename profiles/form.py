from django import forms
from .models import profil
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class WaForm(forms.ModelForm):
    no_wa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nomor WhatsApp'}),
    )
    imageProfil = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'btn btn-info', 'id': 'imageProfil'})
    )
    class Meta:
        model = profil
        fields = ['no_wa', 'imageProfil']
        
class CustomTabelUserForm(UserChangeForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Username'}),
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Email'})
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Nama Depan'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Nama Belakang'})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']