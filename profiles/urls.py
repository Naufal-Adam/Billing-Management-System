from django.urls import path
from . import views

urlpatterns = [
    path('profil/<int:pk>/', views.profil_edit, name='profil_edit'),
]