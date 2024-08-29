from django.shortcuts import render, get_object_or_404

from store.models import Product

class Basket ():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey']= {}
        self.basket = basket

    
    def add(self, product, product_qty):
        product_id= product.id
        self.basket[str(product_id)] = {'price': str(product.price), 'qty': int(product_qty)}
        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values() )
    
    def get_items(self):
        items = []
        for product_id, data in self.basket.items():
            product = get_object_or_404(Product, id=product_id)
            items.append({'product': product, 'qty': data['qty'], 'price': data['price']})
        return items
    
    def get_total_price(self):
        return sum(float(item['price']) * int(item['qty']) for item in self.basket.values())

    



