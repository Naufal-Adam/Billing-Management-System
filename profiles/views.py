from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .form import CustomTabelUserForm, WaForm
from .models import profil

# Create your views here.
def profil_edit(request, pk):
    wa_instance = get_object_or_404(profil, pk=pk)
    if request.method == 'POST':
        form = CustomTabelUserForm(request.POST, instance=request.user)
        formWa = WaForm(request.POST, request.FILES, instance=wa_instance)
        if form.is_valid() and formWa.is_valid():
            form.save()
            formWa.save()
            return redirect('dashboard_njir')
    else:
        form = CustomTabelUserForm(instance=request.user)
        formWa = WaForm(instance=wa_instance)
    return render(request, 'index.html', {'formBiasa' : form, 'formWa' : formWa, 'imageku' : wa_instance})