from django.http import JsonResponse
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerCart
from .serializers import (SubcategorySerializer,
                          CategorySerializer,
                          ProductSerializer,
                          CardSerializer)
from .models import Subcategory, Category, Product, Card
from .mixins import ListMixin


class CategoryViewSet(ListMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ListMixin):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductViewSet(ListMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CardViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerCart, IsAuthenticated,)
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    @action(detail=False, methods=["post"])
    def clear_cart(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.clear_cart()
        return Response({"message": "Все содержимое корзины удалено!"})

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


class TotalPriceViewSet(views.APIView):
    permission_classes = (IsOwnerCart, IsAuthenticated,)

    def get(self, request):
        cards = Card.objects.filter(user=request.user)
        total_price = sum([card.count * card.product.price for card in cards])
        total_products = cards.count()
        return JsonResponse({'total_price': total_price,
                             'товаров в корзине': total_products})
