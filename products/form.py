from django import forms
from .models import produk
from clients.models import client

class ProdukForm(forms.ModelForm):
    nama_produk = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama Produk'})
    )
    type_produk = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Tipe Produk'})
    )

    class Meta:
        model = produk
        fields = ['nama_produk', 'type_produk']
        
class ProdukFormWithDropdown(forms.Form):
    nama_client = forms.ModelChoiceField(queryset=client.objects.all(), empty_label=None)