from django.shortcuts import render

from mainsite.models import Catalog
from product.models import Product


def main(request):
    return render(request, 'demoCart/main.html')


def desktops(request, catalog_id):

    return render(request, 'demoCart/desktops.html',
                  {'catalog': Catalog.objects.all(), 'product': Product.objects.all(),
                   'products_list': Product.objects.filter(catalog_id=catalog_id)})


def laptops_notebooks(request):
    pass


def components(request):
    pass


def tablets(request):
    pass


def software(request):
    pass


def phonespdas(request):
    pass


def cameras(request):
    pass


def mp3players(request):
    pass
