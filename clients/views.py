from django.shortcuts import get_object_or_404, redirect, render
from .models import client, clientAlamat
from .formKhususClient import ClientForm, ClientAlamatForm

# Create your views here.
def client_view(request):
    Client = client.objects.all()
    Alamat = clientAlamat.objects.all()
    return render(request, 'clients-idx.html', {'Client': Client, 'Alamat': Alamat})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        formAlamat = ClientAlamatForm(request.POST)
        if form.is_valid() and formAlamat.is_valid():
            client = form.save()
            alamat = formAlamat.save(commit=False)
            alamat.client = client
            alamat.save()
            return redirect('client_njir')
    else:
        form = ClientForm()
        formAlamat = ClientAlamatForm()
    return render(request, 'add-clients.html', {'form': form, 'formAlamat': formAlamat})

def update_client(request, pk):
    client_instance = get_object_or_404(client, pk=pk)
    alamat_instance = get_object_or_404(clientAlamat, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client_instance)
        formAlamat = ClientAlamatForm(request.POST, instance=alamat_instance)
        if form.is_valid() and formAlamat.is_valid():
            clientpeh = form.save()
            alamat = formAlamat.save(commit=False)
            alamat.client = clientpeh
            alamat.save()
            return redirect('client_njir')
    else:
        form = ClientForm(instance=client_instance)
        formAlamat = ClientAlamatForm(instance=alamat_instance)
    return render(request, 'edit-clients.html', {'form': form, 'formAlamat': formAlamat})

def delete_client(request, pk):
    client_instance = get_object_or_404(client, pk=pk)
    if request.method == 'POST':
        client_instance.delete()
        return redirect('client_njir')
    return render(request, 'clients-idx.html', {'client': client_instance})