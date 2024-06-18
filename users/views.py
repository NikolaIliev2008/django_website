from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm  

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user-profile') 
    else:
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('home'))  
    
    return redirect(reverse('home'))

@login_required
def profile(request):
    return render(request, 'users/profile.html')







    

