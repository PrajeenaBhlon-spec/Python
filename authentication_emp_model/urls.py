from django.urls import path
from . import views

urlpatterns = [
  path('landing/' , views.landing_page),
  path('register/', views.register , name="register"),
  path('login/' , views.loginEmployee , name="login"),
  path('login/hero/' , views.home , name="authenticate_home")
]
