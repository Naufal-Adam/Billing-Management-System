from django.urls import path
from . import views

urlpatterns = [
    path('invoices', views.invoice_view, name='invoice_njir'),
    path('invoices/add', views.add_invoice, name='add_invoice'),
    path('invoices/add/<str:action>/', views.add_invoice, name='add_action'),
    path('invoices/delete/<int:pk>/', views.delete_invoice_produk, name='delete_produk_invoice'),
    path('invoices/send', views.invoice_send, name='invoice_send' ),
]