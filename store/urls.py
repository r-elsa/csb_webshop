from django.urls import path
from . import views

app_name= 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search_products, name='search_products'), 
    path('search/all/', views.all_products, name='all_products'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list')
]