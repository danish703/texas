from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Username'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }),label="Password Confirmation")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
