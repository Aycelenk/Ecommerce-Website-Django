from django.shortcuts import redirect, render,get_object_or_404
from .models import InStockProduct,Category,Comment,Users
from Main.helper_functions import SetNewPriceForOne
from django.contrib import messages

quantity = 0
# Create your views here.
def detail(request,pk):
    anon_user = None
    global quantity
    referrer = request.META.get("HTTP_REFERER")
    if referrer == f"http://127.0.0.1:8000/items/{pk}":
        pass
    else:
        quantity = 0
    product = get_object_or_404(InStockProduct,pk=pk)
    category = get_object_or_404(Category,id = product.category_id)
    comment = None
    comments = Comment.objects.all()
    #
    if request.user.is_authenticated:
        user = request.user
    else:
        user = request.user
        anon_user = user


    if request.method == 'POST':
        if "minus_button" in request.POST:
            current_quantity = request.POST.get("quantity_field")
            if current_quantity == 0:
                # do nothing
                pass
            else:
                quantity -= 1
                return redirect('detail',pk=pk)
        elif "plus_button" in request.POST:
            quantity += 1
            return redirect('detail',pk=pk)
        elif "newdiscount" in request.POST:
            #yeni discount kurdu salesmanager
            product_id = request.POST.get("product_id")
            product = InStockProduct.objects.get(ID = product_id)
            product.discount = int(request.POST.get("newdiscount"))
            SetNewPriceForOne(product)
        elif "newprice" in request.POST:
            #yeni price koydu sales manager
            product_id = request.POST.get("product_id")
            product = InStockProduct.objects.get(ID = product_id)
            product.price = float(request.POST.get("newprice"))
            if product.discount != 0:
                SetNewPriceForOne(product)
            else:
                product.newPrice = 0
                product.save()
        elif "command" in request.POST and request.POST.get("command") == "remove":
            #prduct manager remove product
            product_id = request.POST.get("product_id")
            product = InStockProduct.objects.get(ID = product_id)
            product_name = product.name
            messages.success(request,f"You successfully removed {product_name}")
            product.delete()
            return redirect("index")
        elif "newstock" in request.POST:
            product_id = request.POST.get("product_id")
            product = InStockProduct.objects.get(ID = product_id)
            new_stock = int(request.POST.get("newstock"))
            product.quantity_in_stocks = new_stock
            product.save()
        else:
            stars = request.POST.get('stars', 3)
            content = request.POST.get('content', '')

            comment = Comment.objects.create(product=product, user=request.user, stars=stars, content=content)
            comment.save()
            return redirect('detail',pk=pk)
        
    return render(request,"detail.html",{
            "product":product,
            "category":category,
            "comments":comments,
            "quantity":quantity,
            "user":user,
            "anon_user":anon_user})
