from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet,
                    SubcategoryViewSet,
                    ProductViewSet,
                    CardViewSet,
                    TotalPriceViewSet)

router = DefaultRouter()

router.register('category', CategoryViewSet, basename='category')
router.register('subcategory', SubcategoryViewSet, basename='subcategory')
router.register('product', ProductViewSet, basename='product')
router.register('card', CardViewSet, basename='card')


urlpatterns = [
    path('', include(router.urls)),
    path('total/', TotalPriceViewSet.as_view()),
]
