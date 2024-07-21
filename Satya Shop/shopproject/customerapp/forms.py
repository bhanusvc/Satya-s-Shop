from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fullname', 'gender', 'email', 'username', 'password', 'contact']
        widgets = {
            'password': forms.PasswordInput(),
            'contact': forms.TextInput(attrs={'type': 'tel'}),
        }

    contact = forms.RegexField(
        regex=r'^\+?1?\d{10}$',  # Adjust the regex according to your requirement
        error_messages={
            'invalid': 'Enter a valid contact number. Up to 10 digits allowed.'
        }
    )

