from django import forms
from .models import File
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    username = forms.CharField(label="Username", max_length=150)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
