from django.shortcuts import render, redirect
from .models import Student
from django.http import JsonResponse

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


def delete_student_api(request, id):
  if request.method == "POST":  
    try:
      student = Student.objects.get(id=id)
      student.delete()
      return JsonResponse({"message": "Student deleted successfully!"})
    except Student.DoesNotExist:
      return JsonResponse({"message": "Student not found!"}, status=404)
