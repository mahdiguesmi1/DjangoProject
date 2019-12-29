from collections import defaultdict
from itertools import chain

from django.http import HttpResponse
from django.views.generic import DetailView
from requests import Response
from rest_framework.utils import json

from .models import Product, Category,Comment
from .serializers import ProductSerializer, CommentSerializer, CategorySerializer
from rest_framework import generics
from django.contrib import admin

from rest_framework import viewsets, permissions


class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.request.user.comments.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryListCreate(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter()

    def perform_create(self, serializer):
        serializer.save()



class AllCommentsListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        l=Comment.objects.none()
        nombre =Product.objects.filter().count()
        for product in Product.objects.all() :
            comments=product.comments.values_list(flat=True)
            l=chain(l,comments)

        return l
        








