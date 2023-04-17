from django import forms
from django.contrib import admin

from .models import Users,Category,OrderedProduct,InStockProduct,Comment


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('ID',)

# Register your models here.
admin.site.register(InStockProduct, ProductAdmin)
admin.site.register(OrderedProduct)
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Comment)