from django.shortcuts import render

# Create your views here.
def start_app(request):
  return render(request , 'Home.html')