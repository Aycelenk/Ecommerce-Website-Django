from Product.models import InStockProduct,Users
from Cart.models import Cart

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
            Cart.objects.create(product= product,user= request.user,quantity = 1)
        Users.objects.filter(username = "Anonymous User").delete() 