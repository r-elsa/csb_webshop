from django.shortcuts import render, get_object_or_404
from store.models import Product

class Basket ():
    def __init__(self, request):
        self.session = request.session
        """ basket = self.session.get('skey') """
        
        
        session_id = request.GET.get('session_id', '1') #new 
        basket_key = f'basket_{session_id}'  # Assume session keys are like 'basket_1', 'basket_2', etc.

        """ if 'skey' not in request.session:
            basket = self.session['skey']= {}
        self.basket = basket """
        
        if basket_key not in self.session: # new
            self.session[basket_key] = {} #new
        self.basket = self.session[basket_key] #new

    
    def add(self, product, product_qty):
        product_id = product.id
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

    



