from django.contrib.sessions.models import Session
from django.http import JsonResponse
import json

class Searchresult():
    def __init__(self,request):
        self.session = request.session    
        searchresult = self.session.get('search_results')
     
        if 'search_results' not in request.session:
            searchresult = self.session['search_results'] = {}  
        self.searchresult = searchresult    

    def add(self, res):
        self.session['search_results'] = res 
        self.session.modified = True

    def getproduct_ids(self):
        x = self.session['search_results'].strip('')
        products = json.loads(x)
        product_ids = [product['id'] for product in products]
        return product_ids


        