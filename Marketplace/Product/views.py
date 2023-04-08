from django.shortcuts import render,get_object_or_404
from .models import InStockProduct

# Create your views here.
def detail(request,pk):
    product = get_object_or_404(InStockProduct,pk=pk)
    return render(request,"detail.html",{
        "product":product})


