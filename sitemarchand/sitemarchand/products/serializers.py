from rest_framework import serializers
from .models import Comment, Product, Category


class ProductSerializer(serializers.ModelSerializer):
    serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', 'titre', 'comments', 'description', 'category', 'owner', 'created_at']
        depth = 2


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 2


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
