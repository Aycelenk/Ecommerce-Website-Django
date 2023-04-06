from django.urls import path
from . import views
from .forms import LoginForm


urlpatterns = [
    path("login/",views.login,name = "login"),
    path("",views.index,name="index"),
    path("signup/",views.signup,name = "signup"),
]
