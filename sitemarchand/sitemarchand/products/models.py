from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.views.generic import DetailView


class Category(models.Model):
    label = models.CharField(max_length=30)


class Product(models.Model):
    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE, null=False)
    owner = models.ForeignKey(
        User, related_name="products", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(
        Product, related_name="comments", on_delete=models.CASCADE, null=False)
