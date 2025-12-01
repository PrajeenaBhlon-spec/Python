from django.shortcuts import render , redirect
from .models import Employee
from django.http import JsonResponse
import json
# Create your views here.

def main_page(request):
  return render(request , "Home.html")

def addEmployee(request):
  if request.method == "POST":
    name = request.POST.get("name")
    address = request.POST.get("address")
    empType = request.POST.get("empType")
    salary = request.POST.get("salary")
    
    if name and address and empType and salary:
      employee = Employee(name = name , address = address , empType = empType , salary = salary)
      employee.save()
      return redirect("add-employee")
    
  return render(request , "addEmployee.html")

def display_emp_api(request):
  employees = Employee.objects.all().values()
  return JsonResponse(list(employees) , safe = False)

def displayEmployee(request):
  return render(request , "displayEmployee.html")


def delete_emp_api(request , id):
  if request.method == "POST":
    try:
      employee = Employee.objects.get(id = id)
      employee.delete()
      return JsonResponse({"message": "employee deleted successfully"})
    
    except Employee.DoesNotExist:
      return JsonResponse({"message": "employee not found"})
  
def delete(request):
  return render(request , "deleteEmployee.html")

def update_emp_api(request , id):
  if request.method == "PUT":
    try:
      employee = Employee.objects.get(id = id)
      emp_data = json.loads(request.body)
      name = emp_data.get("name")
      address = emp_data.get("address")
      empType = emp_data.get("empType")
      salary = emp_data.get("salary")
      if name != "":
        employee.name = name
      if address != "":
        employee.address = address
      if empType != "":
        employee.empType = empType
      if salary != "":
        employee.salary = int(salary)

      employee.save()
      return JsonResponse({"message":"Data updated successfully"})
    
    except Employee.DoesNotExist:
      return JsonResponse({"message":"Employee not found"})
    
def update(request):
  return render(request , "updateEmployee.html")