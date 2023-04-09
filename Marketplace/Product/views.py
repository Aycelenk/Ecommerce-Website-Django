from django.shortcuts import render,get_object_or_404
from .models import InStockProduct,Category

# Create your views here.
def detail(request,pk):
    product = get_object_or_404(InStockProduct,pk=pk)
    category = Category.objects.filter(id = product.category_id)
    return render(request,"detail.html",{
        "product":product,
        "category":category})


