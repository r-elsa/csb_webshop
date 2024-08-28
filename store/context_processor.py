from .searchresult import Searchresult 

# making searchresults available throughout the apps

def searchres(request):
    return {'searchresult': Searchresult(request)}   