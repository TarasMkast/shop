from django.shortcuts import render

from cart.forms import CartForm
from .models import Goods, MainCatalog, Catalog, PropertyImage


def main(request):
    return render(request, 'mainsite/main.html', {'list_maincatalog': MainCatalog.objects.all()})


def all_catalog(request):
    return render(request, 'mainsite/allcatalog.html', {'list_catalog': Catalog.objects.all()})


def catalog(request, maincatalog_id):
    return render(request, 'mainsite/catalog.html',
                  {'list_catalog': Catalog.objects.filter(mainCatalog_id=maincatalog_id)})


def goods(request, catalog_id):
    return render(request, 'mainsite/goods.html', {'list_goods': Goods.objects.filter(catalog_id=catalog_id)})


def goodsDetail(request, goods_id):
    cart_form = CartForm
    print(Goods.objects.filter(id=1))
    return render(request,
                  'mainsite/goodsDetail.html',
                  {'list_goods': Goods.objects.filter(id=goods_id),
                   'list_image': PropertyImage.objects.filter(goods_id=goods_id),
                   'cart_form': cart_form})

