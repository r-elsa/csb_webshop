from .searchresult import Searchresult 

def searchres(request):
    return {'searchresult': Searchresult(request)}   