from django.contrib import admin
from .models import InStockProduct, OrderedProduct, User

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('ID',)

# Register your models here.
admin.site.register(InStockProduct, ProductAdmin)
admin.site.register(OrderedProduct)
admin.site.register(User)