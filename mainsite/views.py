from django.shortcuts import render, redirect
from .models import Catalog


def main(request):
    return render(request, 'mainsite/main.html', {'list_catalog': Catalog.objects.all()})



