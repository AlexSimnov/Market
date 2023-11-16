from rest_framework import serializers
from .models import Card, Category, Subcategory, Product
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user',)


class SubcategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(use_url=True)

    class Meta:
        model = Subcategory
        fields = ('name',
                  'slug',
                  'image',)


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many=True)
    image = Base64ImageField(use_url=True)

    class Meta:
        model = Category
        fields = ('name',
                  'slug',
                  'image',
                  'subcategory',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image_big = Base64ImageField()
    image_medium = Base64ImageField()
    image_small = Base64ImageField()

    class Meta:
        model = Product
        fields = ('name',
                  'slug',
                  'category',
                  'price',
                  'image_big',
                  'image_medium',
                  'image_small',)


class CardSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    count = serializers.IntegerField(required=True, min_value=1)
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True
    )

    def create(self, validated_data):
        user = self.context["request"].user
        count = validated_data["count"]
        product = validated_data["product"]

        existed = Card.objects.filter(user=user, product=product)

        if existed:
            existed = existed[0]
            existed.count += count
            existed.save()
        else:
            existed = Card.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        instance.count = validated_data["count"]
        instance.save()
        return instance

    def clear_cart(self):
        user = self.context["request"].user
        Card.objects.filter(user=user).delete()
