from django.urls import path
from . import views

urlpatterns = [
    path('setting', views.setting_view, name='setting_view'),
    path('setting/add-notif', views.add_notif, name='add_notif'),
    path('setting/update/<int:pk>/', views.edit_notif, name='edit_notif'),
]