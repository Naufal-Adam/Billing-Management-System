from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_njir')
        else:
            # Tambahkan pesan error jika login gagal
            error_message = "Username atau password salah"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')
