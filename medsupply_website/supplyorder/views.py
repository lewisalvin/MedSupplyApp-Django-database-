from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm

def home(request):
    thisCustomer = Customer.objects.all()
    return render(request, 'home.html', {'thisCustomer': thisCustomer} )

def register(request):
    return render(request, 'register.html', {} )
