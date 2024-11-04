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
    if request.POST.get('action') == 'post':
        session_id = request.POST.get('session_id', '1') # new
        product_id = int(request.POST.get('product_id', 0))
        product_qty = int(request.POST.get('product_qty', 1))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        basket_qty = len(basket)  
        response = JsonResponse({'qty': basket_qty, 'session_id': session_id}) #  new,  Include the session ID in the response for visibility
        

        duplicates = CustomUser.objects.values('email').annotate(email_count=Count('email')).filter(email_count__gt=1)
        for dup in duplicates:
            print(dup)
        
        for email in duplicates.values_list('email', flat=True):
            users = CustomUser.objects.filter(email=email)
            users_to_delete = users[1:]  # Keep the first one
            users_to_delete.delete()
        return response
