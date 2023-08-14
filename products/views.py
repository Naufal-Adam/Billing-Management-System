from django.shortcuts import get_object_or_404, redirect, render
from .models import produk
from clients.models import client
from .form import ProdukForm, ProdukFormWithDropdown
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
        formDropdown = ProdukFormWithDropdown(request.POST)
        if form.is_valid() and formDropdown.is_valid():
            produk = form.save(commit=False)
            selected_client = formDropdown.cleaned_data['nama_client']
            produk.client = selected_client
            produk.save()
            return redirect('produk_view')
    else:
        form = ProdukForm()
        formDropdown = ProdukFormWithDropdown()
    wa_instance = get_object_or_404(profil)
    return render(request, 'add-products.html', {'form': form, 'imageku': wa_instance, 'formDrop': formDropdown})

def update_produk(request, pk):
    produk_instance = get_object_or_404(produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk_instance)
        formDropdown = ProdukFormWithDropdown(request.POST)
        if form.is_valid() and formDropdown.is_valid():
            produks = form.save(commit=False)
            selected_client = formDropdown.cleaned_data['nama_client']
            produks.client = selected_client
            produks.save()
            return redirect('produk_view')
    else:
        form = ProdukForm(instance=produk_instance)
        formDropdown = ProdukFormWithDropdown()
    wa_instance = get_object_or_404(profil)
    return render(request, 'edit-products.html', {'form': form, 'imageku': wa_instance, 'formDrop': formDropdown})

def delete_produk(request, pk):
    produk_instance = get_object_or_404(produk, pk=pk)
    if request.method == 'POST':
        produk_instance.delete()
        return redirect('produk_view')
    return render(request, 'products-idx.html', {'produk': produk_instance})