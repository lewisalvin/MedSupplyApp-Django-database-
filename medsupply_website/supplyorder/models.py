from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    confirmpasswd = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    insurance = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    dateOfBirth = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    
class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    orderAmount =  models.CharField(max_length=100)
    orderShipName = models.CharField(max_length=100)
    orderShipAddress = models.CharField(max_length=300)
    orderCity = models.CharField(max_length=100)
    orderState = models.CharField(max_length=100)
    orderZip = models.CharField(max_length=100)
    orderPhone = models.CharField(max_length=100)

    def __str__(self):
        return self.orderShipName + ' ' + self.customer_id


class Products(models.Model):
    productSKU = models.CharField(max_length=100, unique=True)
    productName = models.CharField(max_length=100)
    productPrice = models.CharField(max_length=100)
    productStock = models.CharField(max_length=100)

    def __str__(self):
        return self.productName


class OrderDetails(models.Model):
    detailID = models.CharField(max_length=100)
    detailOrderID = models.ForeignKey(Orders, blank=True, null=True, on_delete=models.CASCADE)
    detailProductID = models.ForeignKey(Products, blank=True, null=True, on_delete=models.CASCADE)
    detailName = models.CharField(max_length=100)
    detailPrice = models.CharField(max_length=100)
    detailSKU = models.CharField(max_length=100)
    detailQuantity = models.CharField(max_length=100)

    def __str__(self):
        return self.detailName



