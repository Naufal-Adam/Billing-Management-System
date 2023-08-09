from django.urls import path
from . import views

urlpatterns = [
    path('invoices', views.invoice, name='invoice_njir'),
    path('invoices/add', views.add_invoice, name='add_invoice'),
]