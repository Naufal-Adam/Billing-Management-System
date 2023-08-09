from django.urls import path
from . import views

urlpatterns = [
    path('profil/', views.profil_view, name='profil_view'),
    path('profil/edit/<int:pk>/', views.profil_edit, name='profil_edit'),
]