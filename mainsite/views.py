from django.shortcuts import render, redirect
from .models import MainCatalog, Catalog


def main(request):
    return render(request, 'mainsite/main.html', {'list_maincatalog': MainCatalog.objects.all()})


def all_catalog(request):
    return render(request, 'mainsite/allcatalog.html', {'list_catalog': Catalog.objects.all()})


def catalog(request, maincatalog_id):
    return render(request, 'mainsite/catalog.html',
                  {'list_catalog': Catalog.objects.filter(mainCatalog_id=maincatalog_id)})

