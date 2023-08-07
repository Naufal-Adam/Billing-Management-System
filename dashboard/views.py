from django.shortcuts import get_object_or_404, render
from profiles.models import profil

# Create your views here.
def dashboard(request):
    wa_instance = get_object_or_404(profil)
    return render(request, "dashboard-idx.html", {'imageku': wa_instance})