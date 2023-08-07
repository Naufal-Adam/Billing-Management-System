from django import forms
from .models import client, clientAlamat

class ClientForm(forms.ModelForm):
    nama_client = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama Client'})
    )
    no_wa_client = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Tipe No WA'})
    )
    email_client = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama Email'})
    )
    kode_pos = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Kode Pos'})
    )

    class Meta:
        model = client
        fields = ['nama_client', 'no_wa_client', 'email_client', 'kode_pos']
        
class ClientAlamatForm(forms.ModelForm):
    jalan = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama Jalan'})
    )
    kabupaten = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama Kabupaten'})
    )
    provinsi = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama Provinsi'})
    )

    class Meta:
        model = clientAlamat
        fields = ['jalan', 'kabupaten', 'provinsi']