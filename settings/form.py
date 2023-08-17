from django import forms
from .models import setting, client, produk

class SettingForm(forms.ModelForm):
    date_notif = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control flatpickr-date'})
    )
    time_notif = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control flatpickr-time'})
    )
    text_notif = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '*Dear Admin, its invoice time for....', 'rows': 3})
    )
    checkbox_email = forms.BooleanField(required=False)
    checkbox_sms = forms.BooleanField(required=False)
    to_who = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'})
    )
    to_sms = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+6299999999'})
    )
    class Meta:
        model = setting
        fields = ['date_notif', 'time_notif', 'text_notif', 'to_who', 'to_sms']
        
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
