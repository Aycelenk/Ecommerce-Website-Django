from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

class MyUserManager(UserManager):
    def _create_user(self, email,username,password=None,**extra_fields):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        email = self.normalize_email(email)
        user = self.model(email = email,username = username,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None,username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,username, password,**extra_fields)

    def create_superuser(self,email = None,username = None,password = None,**extra_fields):
        """
        Creates and saves a superuser with the given username, and password.
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,username,password,**extra_fields)

class Users(AbstractBaseUser,PermissionsMixin):
    ID = models.AutoField(primary_key=True)
    email = models.EmailField(blank=True,default='')
    first_name = models.CharField(max_length=30,default='',blank=True)
    last_name = models.CharField(max_length=30,default='',blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=100,unique=True)
    tax_ID = models.IntegerField(default=0)
    home_address = models.TextField(blank=True,null=True)
    role = models.CharField(max_length=100,default='customer')
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True,null=True)

    
    objects = MyUserManager()

    REQUIRED_FIELDS = []

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.username
    


    
class InStockProduct(models.Model):
    ID = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,related_name = "products",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Product/static/img/")
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
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_process_status = models.CharField(max_length=100, default="processing")

    def __str__(self):
        return self.name