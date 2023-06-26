from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from admin_dashboard.models import *


class UserloginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Email Id",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your email Id",
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "confirm Password",
            }
        ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AdminUserUpdateForm(ModelForm):
    class Meta:
        model = AdminUser
        fields = ['name', 'phone', 'email']


class GuestUserUpdateForm(ModelForm):
    class Meta:
        model = GuestUser
        fields = ['name', 'email']


class GuestUserUpdateForm(ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'


class PDFFileForm(ModelForm):
    class Meta:
        model = PDFFile
        fields = '__all__'
