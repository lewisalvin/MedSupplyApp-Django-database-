from django import forms
from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    #allows you to define things in the class.
    class Meta:
        model = Customer
        fields = "__all__"

        labels = {
            'firstName': '',
            'lastName': '',
            'passwd': '',
            'confirmpasswd': '',
            'email': '',
            'insurance': '',
            'phone': '',
            'dateOfBirth': '',
            'city': '',
            'state': '',
            'zip': '',
            'address': ''
        }

        widgets = {
            'firstName': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'passwd': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Password'}),
            'confirmpasswd': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Confirm Password'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
            'insurance': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insurance'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone'}),
            'dateOfBirth': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Date Of Birth'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'State'}),
            'zip': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zip Code'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'})
        }
