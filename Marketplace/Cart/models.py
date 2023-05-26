from django.db import models
from Product.models import Users,InStockProduct,OrderedProduct
# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(InStockProduct,related_name="cart_product",on_delete=models.CASCADE)
    user = models.ForeignKey(Users,related_name="cart_product",on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product} added by {self.user}"

class PurchaseHistory(models.Model):
    product = models.ForeignKey(InStockProduct,related_name="purchase_history",on_delete=models.CASCADE)
    user = models.ForeignKey(Users,related_name="purchase_history",on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product} purchased by {self.user}"
