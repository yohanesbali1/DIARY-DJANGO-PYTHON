from django import forms
from django.contrib.auth.models import User


class LoginValidation(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': 'Username is required'})
    password = forms.CharField(required=True, error_messages={'required': 'Password is required'})
    
    
class RegisterValidation(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': 'Username is required'})
    email = forms.EmailField(required=True, error_messages={'required': 'Email is required', 'invalid': 'Enter a valid email address'})
    password = forms.CharField(required=True, error_messages={'required': 'Password is required'})
    confirm_password = forms.CharField(required=True, error_messages={'required': 'Confirm Password is required'})
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username