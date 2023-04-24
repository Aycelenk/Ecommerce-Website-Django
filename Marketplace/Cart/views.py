from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from Main.helper_functions import check_anonymous_cart_products
from Product.models import InStockProduct,OrderedProduct,Users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        check_anonymous_cart_products(request)
    if request.method == "POST":
        command = request.POST.get("command")
        product_id = request.POST.get("product_id")
        if command == "delete":
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
            quantity = request.POST.get("quantity")
            if product.quantity_in_stocks == 0:
                messages.error(request,f"This item is out of stock. Cannot add this item")
                return redirect('detail',pk=product_id)
            if request.user.is_authenticated:
                cart_item = Cart.objects.create(product= product,user= request.user,quantity = quantity)
                cart_item.save()
            else:
                if Users.objects.filter(username = "Anonymous User").exists():
                    anon_user = Users.objects.get(username = "Anonymous User")
                else:
                    anon_user = Users.objects.create_user(is_active = False,role = "Anonymous User")
                cart_item = Cart.objects.create(product= product,user = anon_user,quantity = quantity)
                cart_item.save()
    cart_items = Cart.objects.all()
    return render(request,"cart.html",{"items":cart_items})

@login_required
def buy(request):
    if request.method == "POST":
        check_anonymous_cart_products(request)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        record_count = OrderedProduct.objects.count()
        product = get_object_or_404(InStockProduct,pk = product_id)
        user = request.user
        ordered_item = OrderedProduct.objects.create(ID = record_count + 1,name= product.name,model=product.model,
        number=product.number,description=product.description,price=product.price,
        warranty_status=product.warranty_status,distributor_info=product.distributor_info,
        order_number=str(record_count + 1),delivery_address = "",recipient=user)
        ordered_item.save()
        Cart.objects.get(product_id = product_id).delete()
        messages.success(request,f"Product is bought successfully.You can check the delivery process in delivery tab")
        product.quantity_in_stocks -= quantity
        product.save()
        return render(request,"buy.html",{"product":product})

