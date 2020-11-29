from django.db import models
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control '}))

class RegisterForm_bak(LoginForm):
    email = forms.EmailField(label='email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']