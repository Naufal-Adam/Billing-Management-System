from django.shortcuts import get_object_or_404, render
from profiles.models import profil

# Create your views here.
def invoice(request):
    return render(request, "invoices-idx.html")

def add_invoice(request):
    return render(request, 'add-invoices.html')