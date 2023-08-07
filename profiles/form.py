from django import forms
from .models import profil
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class WaForm(forms.ModelForm):
    no_wa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nomor WhatsApp', 'id': 'wa', 'disabled' : True})
    )
    imageProfil = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'image', 'disabled': True})
    )
    class Meta:
        model = profil
        fields = ['no_wa', 'imageProfil']
        
class CustomTabelUserForm(UserChangeForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Username', 'id': 'username', 'disabled': True}),
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Email', 'id': 'email', 'disabled' : True})
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Nama Depan', 'id': 'depan', 'disabled' : True})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masuk Nama Belakang', 'id': 'belakang', 'disabled' : True})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']