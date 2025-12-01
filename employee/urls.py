from django.urls import path
from . import views

urlpatterns = [
  path('Home/' , views.main_page),
  path('addEmployee/' , views.addEmployee, name="add-employee"),
  path('api/employees/' , views.display_emp_api ),
  path('displayEmployee/', views.displayEmployee ),
  path('api/employees/delete/<int:id>/' , views.delete_emp_api),
  path('deleteEmployee/' , views.delete),
  path('api/employees/update/<int:id>/' , views.update_emp_api),
  path('updateEmployee/' , views.update)
]