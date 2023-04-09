from django.http import HttpResponse
from django.shortcuts import render,redirect
from Product.models import InStockProduct, OrderedProduct, Users
from .forms import LoginForm,SignupForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
# Create your views here.

def index(request):
    data = {
        "instockproducts": InStockProduct.objects.all(),
        "orderedproducts": OrderedProduct.objects.all(),
        #"users": Users.objects.all()
    }
    return render(request,"index.html", data)


def login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        # databaseden formdaki bilgilerdeki usera ara
        username = form.data.get("username")
        password = form.data.get("password")
        if form.is_valid():
            user = authenticate(request,username = username,password = password)
            if user is not None:
                auth_login(request,user)
                return redirect("/")
            else:
                return HttpResponse(form.error_messages["invalid_login"])
        else:
            print(form.errors)
            return render(request,"login.html",{"form":form})
            
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request,"signup.html",{"form":form})
    else:
        form = SignupForm()
        return render(request,"signup.html",{"form":form})
    
def logout_view(request):
    logout(request)
    return redirect("/")