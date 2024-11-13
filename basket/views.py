from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .basket import Basket
from store.models import Product
from django.db.models import Count
from account.models import CustomUser

def basket_summary(request):
    basket = Basket(request)
    basket_items = basket.get_items() 
    return render(request, 'store/basket/summary.html', {'basket_items': basket_items})

def basket_add(request):
    basket = Basket(request)
    if request.method == 'POST':
        session_id = request.POST.get('session_id', '1')  # remove 
        product_id = int(request.POST.get('product_id', 0))
        product_qty = int(request.POST.get('product_qty', 1))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        basket_qty = len(basket)
        response = JsonResponse({'qty': basket_qty, 'session_id': session_id})
        ## response = JsonResponse({'qty': basket_qty})  add
        return response