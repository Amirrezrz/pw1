from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import RentAd
from .forms import RentAdForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

#@login_required
def dashboard(request):
    ads = RentAd.objects.filter(user=request.user)
    return render(request, 'main/dashboard.html', {'ads': ads})

#@login_required
def rent_create(request):
    if request.method == 'POST':
        form = RentAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('dashboard')
    else:
        form = RentAdForm()
    return render(request, 'main/rent_create.html', {'form': form})
