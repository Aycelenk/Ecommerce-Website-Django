from django.shortcuts import redirect, render,get_object_or_404
from .models import InStockProduct,Category,Comment
from django.urls import reverse

# Create your views here.
def detail(request,pk):
    product = get_object_or_404(InStockProduct,pk=pk)
    category = get_object_or_404(Category,id = product.category_id)
    comment = None
    comments = Comment.objects.all()
    #
    if request.method == 'POST':
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        comment = Comment.objects.create(product=product, user=request.user, stars=stars, content=content)
        comment.save()


        return redirect('detail',pk=pk)

    return render(request,"detail.html",{
            "product":product,
            "category":category,
            "comments":comments})
