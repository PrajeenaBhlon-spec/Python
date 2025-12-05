from django.urls import path
from . import views

urlpatterns = [
  path('landing/' , views.landing_page),
  path('register/', views.register , name="register"),
  path("register/login/" , views.loginEmployee),
  path('login/' , views.loginEmployee , name="login"),
  path('login/hero/' , views.home , name="authenticate_home"),
  path('logout/' , views.logout_user , name="log-out")
]
