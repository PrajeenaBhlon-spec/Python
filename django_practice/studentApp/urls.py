from django.urls import path
from . import views

urlpatterns = [
  path('Home/' , views.home),
  path('addStudent/' , views.start_app , name="start_app"),
  path('api/students/' , views.student_api),
  path('displayStudent/' , views.display ),
  path('api/students/delete/<int:id>/', views.delete_student_api, name="delete-student-api"),
  path('deleteStudent/' ,  views.delete)
]