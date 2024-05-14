from django import forms 
from django.contrib.auth.forms import User

class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']