from django import forms
from .models import client, produk, invoice, invoiceProduk

class InvoiceForm(forms.ModelForm):
    no_invoice = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan No Invoice'})
    )
    invoice_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control flatpickr-date'})
    )
    invoice_due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control flatpickr-date'})
    )
    
    class Meta:
        model = invoice
        fields = ['no_invoice', 'invoice_date', 'invoice_due_date']

class InvoiceAddProdukForm(forms.ModelForm):
    item = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control flatpickr-date', 'placeholder': 'Masukan Item'})
    )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control flatpickr-date', 'placeholder': 'Masukan Quantity'})
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control flatpickr-date', 'placeholder': 'Masukan Price'})
    )
    class Meta:
        model = invoiceProduk
        fields = ['item', 'quantity', 'price']
        
class ClientDropdownForm(forms.Form):
    nama_client = forms.ModelChoiceField(
        queryset=client.objects.all(), 
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control choices-single'}))

class ProdukDropdownForm(forms.Form):
    nama_produk = forms.ModelChoiceField(
        queryset=produk.objects.all(), 
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control choices-single'}))

class SelectedIDDropdownForm(forms.Form):
    client  = forms.ModelChoiceField(
        queryset=invoice.objects.all(), 
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control choices-single'}),
    )