from django import forms
from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    #allows you to define things in the class.
    class Meta:
        model = Customer
        fields = "__all__"
