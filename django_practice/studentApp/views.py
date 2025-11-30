from django.shortcuts import render, redirect
from .models import Student
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
  return render(request , "Home.html")

def start_app(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    age = request.POST.get('age')
    grade = request.POST.get("grade")
    if name and age and grade:
      student = Student(name=name, age=age , grade = grade)
      student.save()
      return redirect('start_app') 

  return render(request , 'addStudent.html')


def student_api(request):
  students = Student.objects.all().values()
  return JsonResponse(list(students) , safe=False)

def display(request):
  return render(request , "displayStudent.html")

def delete(request):
  return render(request , "deleteStudent.html")

def update(request):
  return render(request , "updateStudent.html")

def delete_student_api(request, id):
  if request.method == "POST":  
    try:
      student = Student.objects.get(id=id)
      student.delete()
      return JsonResponse({"message": "Student deleted successfully!"})
    except Student.DoesNotExist:
      return JsonResponse({"message": "Student not found!"}, status=404)
    

def update_student_api(request , id ):
  if request.method == "PUT":
    try: 
      student = Student.objects.get(id = id)
      data = json.loads(request.body)
      name = data.get("name")
      age = data.get("age")
      grade = data.get("grade")
      if name != "":
        student.name = name 
      if age != "":
        student.age = age
      if grade != "":
        student.grade = grade
      student.save()
      return JsonResponse({"message": "student updated succesfully"})
    
    except Student.DoesNotExist:
      return JsonResponse({"message": "Student not found"})
  
