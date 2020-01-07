from collections import defaultdict
from itertools import chain
import tensorflow as tf
from django.views.generic import DetailView
from rest_framework.response import Response
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
    queryset = Product.objects.all()
    def list(self, request):
        l=[]
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        for product in queryset :
            comments=product.comments.filter()
            serializer = CommentSerializer(comments, many=True)
            l.append(serializer)



        l=CommentSerializer(l,many=True)
        return Response(l.data)







