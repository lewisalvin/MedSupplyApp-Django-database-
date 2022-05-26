from django.shortcuts import render, redirect
from .models import Customer, Orders, Products
from .forms import CustomerForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout as logouts

def home(request):
    thisCustomer = Customer.objects.all()
    return render(request, 'home.html', {'thisCustomer': thisCustomer} )

def register(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            passwd = form.cleaned_data.get('passwd')
            confirmpasswd = form.cleaned_data.get('confirmpasswd')
            if Customer.objects.filter(email=email).exists():
                messages.error(request, "Email already in use pleigh boy!")
                return redirect('register')
            if passwd != confirmpasswd:
                messages.error(request, "Your passwords don't match mane!")
                return redirect('register')
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register.html', {'form': form, 'submitted': submitted} )


def place_order(request):
    showProducts = Products.objects.all()
    return render(request, 'place_order.html', {'showProducts': showProducts} )


def product_breakdown(request, products_id):
    product = Products.objects.get(pk=products_id)
    return render(request, 'product_breakdown.html', {'product': product,} )

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('register')


