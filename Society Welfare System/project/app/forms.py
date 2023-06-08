
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from .models import *

class fileUploadForm(forms.Form):
    username = forms.CharField(max_length=30)
    department = forms.CharField(max_length=30)
    address = forms.CharField(max_length=100)
    issue = forms.CharField(max_length=100)
    file = forms.FileField()


# forms.py


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
