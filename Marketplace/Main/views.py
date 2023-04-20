from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from Product.models import InStockProduct, OrderedProduct,Users,Category
from .forms import LoginForm,SignupForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from threading import Thread
from delivery import delivered,in_transit
# Create your views here.

def index(request):
    data = {
        "instockproducts": InStockProduct.objects.all(),
        "orderedproducts": OrderedProduct.objects.all(),
        #"users": Users.objects.all()
        "categories":Category.objects.all()
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
            return render(request,"login.html",{"form":form})
            
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Account created for {request.POST.get('username')}")
            return redirect("login")
        else:
            return render(request,"signup.html",{"form":form})
    else:
        form = SignupForm()
        return render(request,"signup.html",{"form":form})
    
def logout_view(request):
    logout(request)
    return redirect("/")

def delivery(request):
    if request.method == "POST":
        command = request.POST.get("command")
        product_id = request.POST.get("product_id")
        if command == "delete":
            OrderedProduct.objects.get(ID = product_id).delete()
    ordered_products = OrderedProduct.objects.all()
    return render(request,"delivery.html",{"products":ordered_products})