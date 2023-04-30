from Product.models import InStockProduct,Users
from Cart.models import Cart
from django.shortcuts import get_object_or_404

def check_anonymous_cart_products(request):
    anon_user = None
    if Users.objects.filter(username = "Anonymous User").exists():
        #If there is an Anonymous user, assign it
        anon_user = Users.objects.get(username = "Anonymous User")

    if Cart.objects.filter(user = anon_user).exists():
        #If there is a cart item(s) that belonged to anonymous user, delete that and
        #create a new cart item with the logged in user
        for item in Cart.objects.filter(user = anon_user):
            product = item.product
            Cart.objects.create(product= product,user= request.user,quantity = item.quantity)
        Users.objects.filter(username = "Anonymous User").delete() 

def get_products_from_cart_object(cart_items):
    products = []
    count = Cart.objects.count()
    if count == 0:
        return products
    else:
        for item in cart_items:
            product = get_object_or_404(InStockProduct,pk = item.product)
            products.append(product)
        return products
    
def price_quantity(cart_items):
    d = {}
    for item in cart_items:
       product = get_object_or_404(InStockProduct,pk = item.product)
       price = item.quantity * product.price
       d[f"{item.product}"] = price 
    return d
    
def total_price(cart_items):
    total = None
    for item in cart_items:
        product = get_object_or_404(InStockProduct,pk = item.product)
        price = item.quantity * product.price
        total += price
    if total is None:
        return 0
    else:
        return total