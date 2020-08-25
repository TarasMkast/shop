
from django.conf import settings
from mainsite.models import Goods


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, goods, quantity=1, update_quantity=False):

        goods_id = str(goods.id)
        if goods_id not in self.cart:
            self.cart[goods_id] = {'id': str(goods_id),
                                   'name': str(goods.name),
                                   'quantity': 0,
                                   'price': str(goods.price)}
        if update_quantity:
            self.cart[goods_id]['quantity'] = quantity
        else:
            self.cart[goods_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, goods):
        goods_id = str(goods.id)
        if goods_id in self.cart:
            del self.cart[goods_id]
            self.save()

    def __iter__(self):
        goods_ids = self.cart.keys()
        goodses = Goods.objects.filter(id__in=goods_ids)
        for goods in goodses:
            self.cart[str(goods.id)]['product'] = goods

        for item in self.cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):

        return sum(
            (float(item['price'].replace('₴', '').replace(',', '').replace('.', '')))/100 * item['quantity'] for
            item in
            self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
