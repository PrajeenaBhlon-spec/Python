from django.urls import path
from . import views

urlpatterns = [
  path('Home/' , views.start_app , name="start_app")
]