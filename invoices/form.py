from django import forms
from .models import client
from .models import produk
from .models import invoice

class InvoiceForm(forms.ModelForm):
    no_invoice = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'No Invoice'})
    )
    item = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item'})
    )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'})
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'})
    )
    subtotal = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Subtotal'})
    )
    total = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'})
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'})
    )
    
    class Meta:
        model = invoice
        fields = ['no_invoice', 'item', 'quantity', 'price', 'subtotal', 'total', 'date']
        
class ClientDropdownForm(forms.Form):
    nama_client = forms.ModelChoiceField(queryset=client.objects.all(), empty_label=None)

class ProdukDropdownForm(forms.Form):
    nama_produk = forms.ModelChoiceField(queryset=produk.objects.all(), empty_label=None)