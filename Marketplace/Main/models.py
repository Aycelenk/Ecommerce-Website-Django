from django.db import models

# Create your models here.

class User(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tax_ID = models.IntegerField(default=0)
    email_address = models.CharField(max_length=150)
    home_address = models.TextField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.ID
    
class InStockProduct(models.Model):
    ID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="Main/static/img/")
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.TextField()
    quantity_in_stocks = models.IntegerField()
    price = models.FloatField(default=0)
    warranty_status = models.CharField(max_length=100)
    distributor_info = models.TextField()

    def __str__(self):
        return self.name

class OrderedProduct(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.TextField()
    price = models.FloatField(default=0)
    warranty_status = models.CharField(max_length=100)
    distributor_info = models.TextField()
    order_number = models.CharField(max_length=100)
    delivery_address = models.TextField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    order_process_status = models.CharField(max_length=100, default="processing")

    def __str__(self):
        return self.name
