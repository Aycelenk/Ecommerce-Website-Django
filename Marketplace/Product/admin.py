from django.contrib import admin

# Register your models here.
from .models import InStockProduct,OrderedProduct,User,Category

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('ID',)

# Register your models here.
admin.site.register(InStockProduct, ProductAdmin)
admin.site.register(OrderedProduct)
admin.site.register(User)
admin.site.register(Category)