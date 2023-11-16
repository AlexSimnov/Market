from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        'наименование',
        max_length=150,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False
    )
    image = models.ImageField(upload_to='category_images/')


class Subcategory(models.Model):
    name = models.CharField(
        'наименование',
        max_length=150,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False
    )
    image = models.ImageField(
        upload_to='subcategory_images/'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategory',
    )


class Product(models.Model):
    name = models.CharField(
        'наименование',
        max_length=150,
        blank=False,
        null=False
    )
    slug = models.SlugField(
        unique=True,
        max_length=150,
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='product_category',
        null=True,
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.SET_NULL,
        related_name='product_subcategory',
        null=True,
    )
    price = models.PositiveSmallIntegerField()
    image_big = models.ImageField(
        null=True,
        blank=True,
    )
    image_medium = models.ImageField(
        null=True,
        blank=True,
    )
    image_small = models.ImageField(
        null=True,
        blank=True,
    )


class Card(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='card_owner',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='card_product',
    )
    count = models.PositiveIntegerField()
