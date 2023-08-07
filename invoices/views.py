from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "invoices-idx.html",)

def store(request):
    return render(request, "add-invoices.html")

def send(request):
    return render(request, "send-invoices.html")