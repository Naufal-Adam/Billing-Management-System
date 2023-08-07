from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "setting-idx.html")
def store(request):
    return render(request, "add-notification.html")
def show(request, id):
    return render(request, "",)
def update(request):
    return render(request, "edit-notification.html")
def destroy(request):
    return render(request, "",)