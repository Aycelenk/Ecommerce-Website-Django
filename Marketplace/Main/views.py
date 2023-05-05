from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Product.models import InStockProduct, OrderedProduct,Users,Category
from .forms import LoginForm,SignupForm
from .helper_functions import check_anonymous_cart_products
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        check_anonymous_cart_products(request)
    if request.method == "POST":
        query = request.POST.get("search_field")
        command = request.POST.get("command")
        categories = Category.objects.all()
        if command == "search":
            try:
                searched_product = InStockProduct.objects.get(description__icontains=query)
                category_id = searched_product.category_id
                items = InStockProduct.objects.all()
            except:
                resault = None
            try:
                if category_id:
                    items = items.filter(category_id=category_id)
            except:
                items = None

            if query:
                try:
                    items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
                except:
                    items = None

            return render(request, 'index.html', {
                "instockproducts": items,
                "categories": categories
            })
        else:
            all_products = InStockProduct.objects.all()
            sorted_products = sorted(all_products, key=lambda x: x.price, reverse=True)
            messages.success(request, "Items sorted via price in descending order successfully")
            return render(request, 'index.html', {
                "instockproducts": sorted_products,
                "categories": categories
            })

    if request.user.is_staff == True and request.user.is_superuser == True:
        return redirect("logout")
    data = {
        "instockproducts": InStockProduct.objects.all(),
        "orderedproducts": OrderedProduct.objects.all(),
        # "users": Users.objects.all()
        "categories": Category.objects.all()
    }
    return render(request, "index.html", data)

def login(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        # databaseden formdaki bilgilerdeki usera ara
        username = form.data.get("username")
        password = form.data.get("password")
        if form.is_valid():
            user = authenticate(request,username = username,password = password)
            if user is not None:
                auth_login(request,user)
                next_url = request.POST.get("next")
                if next_url:
                    return redirect("cart")
                else:
                    return redirect("index")
            else:
                return HttpResponse(form.error_messages["invalid_login"])
        else:
            return render(request,"login.html",{"form":form,"next":next_url})
            
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form,"next":next_url})

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