from django.contrib.sessions.models import Session
from django.http import JsonResponse
import json

# Storing search results in session data for possible future sorting

class Searchresult():

    # initializing empty searchresults dictionary if no search done previously
    def __init__(self,request):
        self.session = request.session    
        searchresult = self.session.get('search_results')
     
        if 'search_results' not in request.session:
            searchresult = self.session['search_results'] = {}  
        self.searchresult = searchresult    


    # function search_products in products/views.py runs this function to add searchresult to session
    def add(self, res):
        self.session['search_results'] = res 
        self.session.modified = True
      
    # retrieve ids of previous searchresult from  session 
    def getproduct_ids(self):
        x = self.session['search_results'].strip('')
        products = json.loads(x)
        product_ids = [product['id'] for product in products]
        return product_ids


        