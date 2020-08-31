from django.shortcuts import render
from cart.forms import CartForm
from product.models import Product, PropertyImage


def product_list(request, catalog_id):
    return render(request, 'product/product_list.html', {'product_list': Product.objects.filter(catalog_id=catalog_id)})


def productDetail(request, product_id):
    cart_form = CartForm
    return render(request,
                  'product/productDetail.html',
                  {'product_list': Product.objects.filter(id=product_id),
                   'image_list': PropertyImage.objects.filter(product_id=product_id),
                   'cart_form': cart_form})
