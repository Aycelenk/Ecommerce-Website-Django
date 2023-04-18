from django.shortcuts import render
from .models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart(request):
    cart_items = Cart.objects.all()
    return render(request,"cart.html",{"items":cart_items})