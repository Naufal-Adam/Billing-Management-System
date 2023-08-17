from django.shortcuts import get_object_or_404, redirect, render
from .form import SettingForm, ProdukDropdownForm, ClientDropdownForm
from profiles.models import profil
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from . import keys
from .models import setting


# Create your views here.
def setting_view(request):
    notif = setting.objects.all()
    Profil = get_object_or_404(profil)
    return render(request, "setting-idx.html", {'imageku':Profil, 'notif':notif})

def add_notif(request):
    if request.method == "POST":
        client = Client(keys.account_sid, keys.auth_token)
        form = SettingForm(request.POST)
        formProdukDrop = ProdukDropdownForm(request.POST)
        formClientDrop = ClientDropdownForm(request.POST)
        if form.is_valid() and formProdukDrop.is_valid() and formClientDrop.is_valid():
            date = form.cleaned_data['date_notif']
            time = form.cleaned_data['time_notif']
            text = form.cleaned_data['text_notif']
            selected_client = formClientDrop.cleaned_data['nama_client']
            selected_produk = formProdukDrop.cleaned_data['nama_produk']
            email = form.cleaned_data['checkbox_email']
            sms = form.cleaned_data['checkbox_sms']
            to_email = []
            to_sms = ""
            if email:
                to_email = [form.cleaned_data['to_who']]
                send_mail(
                subject=settings.EMAIL_HOST_USER,
                message=text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=to_email
                )
            if sms:
                to_sms = form.cleaned_data['to_sms']
                message = client.messages.create(
                body=text,
                from_=keys.twilio_number,
                to=to_sms,
                )
            if email or sms:
                setting = form.save(commit=False)
                setting.date = date
                setting.time = time
                setting.text = text
                setting.to_email = to_email
                setting.to_sms = to_sms
                setting.client = selected_client
                setting.produk = selected_produk
                setting.save()
                return redirect('setting_view')
    else:
        form = SettingForm()
        formProdukDrop = ProdukDropdownForm()
        formClientDrop = ClientDropdownForm()
    Profil = get_object_or_404(profil)
    return render(request, 'add-notification.html', {'form': form, 'formProdukDrop': formProdukDrop, 
                                                     'formClientDrop': formClientDrop, 'imageku':Profil})

def edit_notif(request, pk):
    notif_instance = get_object_or_404(setting, pk=pk)
    if request.method == 'POST':
        client = Client(keys.account_sid, keys.auth_token)
        form = SettingForm(request.POST, instance=notif_instance)
        formProdukDrop = ProdukDropdownForm(request.POST)
        formClientDrop = ClientDropdownForm(request.POST)
        if form.is_valid() and formProdukDrop.is_valid() and formClientDrop.is_valid():
            date = form.cleaned_data['date_notif']
            time = form.cleaned_data['time_notif']
            text = form.cleaned_data['text_notif']
            selected_client = formClientDrop.cleaned_data['nama_client']
            selected_produk = formProdukDrop.cleaned_data['nama_produk']
            email = form.cleaned_data['checkbox_email']
            sms = form.cleaned_data['checkbox_sms']
            to_email = []
            to_sms = ""
            if email:
                to_email = [form.cleaned_data['to_who']]
                send_mail(
                subject=settings.EMAIL_HOST_USER,
                message=text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=to_email
                )
            if sms:
                to_sms = form.cleaned_data['to_sms']
                message = client.messages.create(
                body=text,
                from_=keys.twilio_number,
                to=to_sms,
                )
            if email or sms:
                settingg = form.save(commit=False)
                settingg.date = date
                settingg.time = time
                settingg.text = text
                settingg.to_email = to_email
                settingg.to_sms = to_sms
                settingg.client = selected_client
                settingg.produk = selected_produk
                settingg.save()
                return redirect('setting_view')
    else:
        form = SettingForm(instance=notif_instance)
        formProdukDrop = ProdukDropdownForm()
        formClientDrop = ClientDropdownForm()
    Profil = get_object_or_404(profil)
    return render(request, 'edit-notification.html', {'form': form, 'formProdukDrop': formProdukDrop, 
                                                     'formClientDrop': formClientDrop, 'imageku':Profil})