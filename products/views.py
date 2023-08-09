from django.shortcuts import get_object_or_404, redirect, render
from .models import produk
from clients.models import client
from clients.formKhususClient import ClientForm
from .form import ProdukForm
from profiles.models import profil

# Create your views here.
def produk_view(request):
    Produk = produk.objects.all()
    Client = client.objects.all()
    wa_instance = get_object_or_404(profil)
    return render(request, 'products-idx.html', {'Produk': Produk, 'Client':Client, 'imageku': wa_instance})

def add_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        formDropdown = ClientForm(request.POST)
        if form.is_valid() and formDropdown.is_valid:
            form.save()
            return redirect('produk_view')
    else:
        form = ProdukForm()
        formDropdown = ClientForm()
    clients = client.objects.all()
    wa_instance = get_object_or_404(profil)
    return render(request, 'add-products.html', {'form': form, 'clients': clients, 'imageku': wa_instance})

def update_produk(request, pk):
    produk_instance = get_object_or_404(produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk_instance)
        if form.is_valid():
            form.save()
            return redirect('produk_view')
    else:
        form = ProdukForm(instance=produk_instance)
    clients = client.objects.all()
    wa_instance = get_object_or_404(profil)
    return render(request, 'edit-products.html', {'form': form, 'clients': clients, 'imageku': wa_instance})

def delete_produk(request, pk):
    produk_instance = get_object_or_404(produk, pk=pk)
    if request.method == 'POST':
        produk_instance.delete()
        return redirect('produk_view')
    return render(request, 'products-idx.html', {'produk': produk_instance})