from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('<int:product_id>/add/', views.cart_add, name='add_cart'),
    path('<int:product_id>/remove/', views.cart_remove, name='cart_remove'),

]
