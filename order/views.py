from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderForm
from .models import OrderProduct, Order
from product.models import Product


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order = form.save()
        for item in cart:
            OrderProduct.objects.create(
                order=order,
                product=Product.objects.get(id=item['id']),
                price=item['price'].replace(',', ''),
                quantity=item['quantity']
            )
        cart.clear()
        return redirect('order:order_done')
    else:
        form = OrderForm(request.POST)
    return render(request, 'order/order.html', {'form': form,
                                                'cart': cart,
                                                'get_total_price': cart.get_total_price()})


def done(request):
    return render(request, 'order/order_done.html')
