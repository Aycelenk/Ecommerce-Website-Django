from django.shortcuts import render,redirect
from Product.models import InStockProduct, OrderedProduct, Users
from .forms import LoginForm,SignupForm
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
    data = {
        "instockproducts": InStockProduct.objects.all(),
        "orderedproducts": OrderedProduct.objects.all(),
        "users": Users.objects.all()
    }
    return render(request,"index.html", data)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # databaseden formdaki bilgilerdeki usera ara
        if form.is_valid():
            username = form.username
            password = form.password
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect("/")
        else:
            return render(request,"login.html",{"form":form})
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request,"signup.html",{"form":form})
    else:
        form = SignupForm()
        return render(request,"signup.html",{"form":form})