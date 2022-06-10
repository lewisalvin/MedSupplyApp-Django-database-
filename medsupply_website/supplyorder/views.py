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

            #pull in user input email, pw and confirm pw
            email = form.cleaned_data.get('email')
            passwd = form.cleaned_data.get('passwd')
            confirmpasswd = form.cleaned_data.get('confirmpasswd')

            #check to see if email has already been used.
            if Customer.objects.filter(email=email).exists():
                messages.error(request, "Email already in use pleigh boy!")
                return redirect('register')

            #check to make sure confirmed pw matches pw
            if passwd != confirmpasswd:
                messages.error(request, "Your passwords don't match mane!")
                return redirect('register')

            form.save()
            #redirects to register page but makes aware that user has submitted the form successfully.
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register.html', {'form': form, 'submitted': submitted} )


def place_order(request):
    showProducts = Products.objects.all()
    return render(request, 'place_order.html', {'showProducts': showProducts} )

#When product link clicked, redirects to new page to display details of product.
def product_breakdown(request, products_id):
    product = Products.objects.get(pk=products_id)
    return render(request, 'product_breakdown.html', {'product': product,} )

#Code that takes search bar entries and searches database for matches.
def search_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Products.objects.filter(productName__contains=searched)
        return render(request, 'search_products.html', {'searched': searched, 'products': products,} )
    else:
        return render(request, 'search_products.html', {} )

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('register')


