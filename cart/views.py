from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartForm
from mainsite.models import Goods


@require_POST
def cart_add(request, goods_id):
    cart = Cart(request)
    goods = get_object_or_404(Goods, id=goods_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(goods=goods,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, goods_id):
    cart = Cart(request)
    goods = get_object_or_404(Goods, id=goods_id)
    cart.remove(goods)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    # print(cart.get_total_price())
    return render(request, 'cart/detail.html', {'cart': cart, 'total_price': cart.get_total_price()})
