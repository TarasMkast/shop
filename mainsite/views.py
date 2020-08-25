from django.shortcuts import render, redirect

from cart.cart import Cart
from cart.forms import CartForm
from .forms import OrderForm
from .models import Goods, MainCatalog, Catalog, PropertyImage, OrderProduct


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


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order = form.save()
        for item in cart:
            OrderProduct.objects.create(order=order,
                                        goods=Goods.objects.get(id=item['id']),
                                        price=item['price'].replace('₴', '').replace(',', ''),
                                        quantity=item['quantity']
                                        )
        cart.clear()
        return redirect('mainsite:order_done')
    else:
        form = OrderForm(request.POST)
    return render(request, 'mainsite/order.html', {'form': form,
                                                   'cart': cart,
                                                   'get_total_price': cart.get_total_price()})


def done(request):
    return render(request, 'mainsite/order_done.html')
