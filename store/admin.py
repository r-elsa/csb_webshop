from django.contrib import admin

# Register your models here.

from .models import Category, Product

@admin.register(Category) # tell django that we want to register model
class CategoryAdmin(admin.ModelAdmin): # give it more instructions
    list_display= ['name', 'slug' ] # tel Django what fields to show in he list 
    prepopulated_fields={'slug': ('name',)}


@admin.register(Product) # tell django that we want to register model
class ProductAdmin(admin.ModelAdmin): # give it more instructions
    list_display= ['title','author', 'slug', 'price', 'in_stock', 'created', 'updated' ] # tel Django what fields to show in he list 
    list_filter=['in_stock', 'is_active']
    list_editable=['price', 'in_stock']
    prepopulated_fields={'slug': ('title',)}