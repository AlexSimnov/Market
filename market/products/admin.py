from django.contrib import admin
from .models import Subcategory, Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('slug',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
