from decimal import Decimal

from product.models import Product


class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty_item):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id
        if str(product_id) not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty_item)}
        else:
            self.basket[str(product_id)]['qty'] = qty_item + self.basket[str(product_id)]['qty']
        self.save()

    def update(self, product, qty):
        """
        Update qty item in basket
        """
        self.basket[str(product)]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product_id):
        if str(product_id) in self.basket:
            del self.basket[str(product_id)]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return product
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['qty'])
            yield item

    def __len__(self):
        return len(self.basket)
