from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from Product.models import InStockProduct
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def cart(request,product_id = None):
    print(request.META.get('HTTP_REFERER'))
    if product_id is not None:
        if request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/cart/":
            #delete that item from cart
            Cart.objects.get(product_id = product_id).delete()
            messages.success(request,f"Item deleted succesfully")
            return redirect("cart")
        else:
            record_count = Cart.objects.count()
            if record_count != 0:
                if Cart.objects.filter(product_id = product_id).exists():
                    messages.error(request,f"This item is already in your cart. Cannot add this item")
                    return redirect('detail',pk=product_id)
            product = get_object_or_404(InStockProduct,pk = product_id)
            cart_item = Cart.objects.create(product= product,user= request.user,quantity = 1)
            cart_item.save()
    cart_items = Cart.objects.all()
    return render(request,"cart.html",{"items":cart_items})