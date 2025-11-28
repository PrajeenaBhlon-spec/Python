from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def start_app(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    age = request.POST.get('age')
    if name and age:
      student = Student(name=name, age=age)
      student.save()
      return redirect('start_app') 

  return render(request , 'Home.html')

