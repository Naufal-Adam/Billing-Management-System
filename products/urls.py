from django.urls import path
from . import views

urlpatterns = [
    path('produk', views.produk_view, name='produk_view'),
    path('produk/add', views.add_produk, name='add_produk'),
    path('produk/update/<int:pk>/', views.update_produk, name='update_produk'),
    path('produk/delete/<int:pk>/', views.delete_produk, name='delete_produk'),
]