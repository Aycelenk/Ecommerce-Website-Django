from django.shortcuts import render
from Product.models import InStockProduct, OrderedProduct, User

# Create your views here.

def index(request):
    data = {
        "instockproducts": InStockProduct.objects.all()
        #"orderedproducts": OrderedProduct.objects.all(),
        #"users": User.objects.all()
    }
    return render(request,"index.html", data)

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")