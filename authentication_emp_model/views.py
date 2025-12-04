from django.shortcuts import render , redirect
from .models import CustomUser
from django.contrib.auth import authenticate , login


def landing_page(request):
  return render(request , 'landing.html')

def register(request):
  if request.method == "POST":
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    CustomUser.objects.create_user(email=email , username = username , password = password , is_active = True)
    return redirect('login/')
  
  return render(request , "register.html")

def loginEmployee(request):
  if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password , is_active = True)
    if user is not None:
      login(request, user)
      return redirect('hero/')
    else:
      return render(request, "login.html")
  return render(request, "login.html")


def home(request):
  return render(request , "hero.html")