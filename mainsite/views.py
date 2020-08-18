from django.shortcuts import render, get_object_or_404
from .models import Goods, MainCatalog, Catalog, PropertyImage


def main(request):
    list_maincatalog = MainCatalog.objects.all()
    return render(request, 'mainsite/main.html', {'list_maincatalog': list_maincatalog})


def catalog(request, maincatalog_id):
    list_catalog = Catalog.objects.filter(mainCatalog_id=maincatalog_id)
    return render(request, 'mainsite/catalog.html', {'list_catalog': list_catalog})


def goods(request, catalog_id):
    list_goods = Goods.objects.filter(catalog_id=catalog_id)
    return render(request, 'mainsite/goods.html', {'list_goods': list_goods})


def goodsDetail(request, goods_id):
    print(PropertyImage.objects.filter(goods__catalog__mainCatalog_id=goods_id))
    print(PropertyImage.objects.values())
    return render(request,
                  'mainsite/goodsDetail.html',
                  {'list_goods': Goods.objects.filter(id=goods_id),
                   'list_image': PropertyImage.objects.filter(goods__catalog__mainCatalog_id=goods_id)})
