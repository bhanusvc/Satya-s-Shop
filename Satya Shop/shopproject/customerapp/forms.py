from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fullname', 'gender', 'email', 'username', 'password', 'contact']
        widgets = {
            'password': forms.PasswordInput(),
        }
