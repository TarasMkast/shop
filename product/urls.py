from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('<int:product_id>/product/', views.productDetail, name='productDetail'),
    path('<int:catalog_id>/catalog/', views.product_list, name='product_list'),
]
