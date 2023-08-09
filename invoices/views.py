from django.shortcuts import get_object_or_404, redirect, render
from profiles.models import profil
from clients.models import client
from products.models import produk
from .form import InvoiceForm, ClientDropdownForm, ProdukDropdownForm

# Create your views here.
def invoice(request):
    return render(request, "invoices-idx.html")

def add_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        formClientDrop = ClientDropdownForm(request.POST)
        formProdukDrop = ProdukDropdownForm(request.POST)
        if form.is_valid() and formClientDrop.is_valid() and formProdukDrop.is_valid():
            form.save()
            return redirect('add_invoice')
        else:
            form = InvoiceForm()
            formClientDrop = ClientDropdownForm()
            formProdukDrop = ProdukDropdownForm()
    Produk = produk.objects.all()
    Client = client.objects.all()
    return render(request, 'add-invoices.html', {'client': Client, 'produk': Produk, 'form': form })