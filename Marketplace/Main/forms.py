from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from Product.models import Users

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Your username",
        "class":"form-control form-control-lg"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Your password",
        "class":"form-control form-control-lg"
    }))


# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username','email','password1','password2')

