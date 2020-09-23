from django.shortcuts import render
from cart.forms import CartForm
from product.models import Product, PropertyImage


def product_list(request, catalog_id):
    products = Product.objects.filter(catalog_id=catalog_id)
    # image = PropertyImage.objects.filter(product__name__in=products.values_list('name'))
    # image = PropertyImage.objects.get(product__name__in=products.get('name'))
    return render(request, 'product/product_list.html', {'product_list': products})



def productDetail(request, product_id):
    cart_form = CartForm
    return render(request,
                  'product/productDetail.html',
                  {'product_list': Product.objects.filter(id=product_id),
                   'image_list': PropertyImage.objects.filter(product_id=product_id),
                   'cart_form': cart_form})
