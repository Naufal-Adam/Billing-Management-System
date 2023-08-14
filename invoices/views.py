from django.shortcuts import get_object_or_404, redirect, render
from profiles.models import profil
from .form import InvoiceForm, ClientDropdownForm, ProdukDropdownForm, InvoiceAddProdukForm, SelectedIDDropdownForm
from .models import invoice, invoiceProduk

# Create your views here.
def invoice_view(request):
    wa_instance = get_object_or_404(profil)
    return render(request, "invoices-idx.html", {'imageku': wa_instance})

def add_invoice(request, action=None):
    formBiasa = InvoiceForm(request.POST)
    formPro = InvoiceAddProdukForm(request.POST)
    formClientDrop = ClientDropdownForm(request.POST)
    formProdukDrop = ProdukDropdownForm(request.POST)
    invPro = invoiceProduk.objects.all()
    if request.method == 'POST':
        if action == 'add-invoice' and formBiasa.is_valid() and formClientDrop.is_valid():
            invoices = formBiasa.save(commit=False)
            selected_client = formClientDrop.cleaned_data['nama_client']
            invoices.client = selected_client
            invoices.save()
            return redirect('add_invoice')
        elif action == 'add-produk' and formPro.is_valid() and formProdukDrop.is_valid():
            invoicePro = formPro.save(commit=False)
            selected_produk = formProdukDrop.cleaned_data['nama_produk']
            invoicePro.produk = selected_produk
            invoicePro.save()
            return redirect('add_invoice')
    else:
        formBiasa = InvoiceForm()
        formClientDrop = ClientDropdownForm()
        formPro = InvoiceAddProdukForm()
        formProdukDrop = ProdukDropdownForm()
    wa_instance = get_object_or_404(profil)
    return render(request, 'add-invoices.html',{'form': formBiasa, 'formDropClient': formClientDrop,
                                                'formPro': formPro,'formDropProduk': formProdukDrop,
                                                'pro': invPro, 'imageku': wa_instance})

def delete_invoice_produk(request, pk):
    produkInv_instance = get_object_or_404(invoiceProduk, pk=pk)
    if request.method == 'POST':
        produkInv_instance.delete()
        return redirect('add_invoice')
    return render(request, 'add-invoices.html', {'produkInv': produkInv_instance})

def invoice_send(request):
    if request.method == 'POST':
        form = SelectedIDDropdownForm(request.POST)
        if form.is_valid():
            selected_invoice = form.cleaned_data['invoice']
            nama_client = selected_invoice.client.nama_client
            context = {'selected_invoice': selected_invoice, 'nama_client': nama_client}
            return render(request, 'send-invoices.html', context)
    else:
        form = SelectedIDDropdownForm()
    wa_instance = get_object_or_404(profil)
    return render(request, 'send-invoices.html', {'imageku': wa_instance, 'form': form})