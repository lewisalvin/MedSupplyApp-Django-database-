from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('place_order', views.place_order, name="place_order"),
    path('product_breakdown/<products_id>', views.product_breakdown, name="product_breakdown"),

]
