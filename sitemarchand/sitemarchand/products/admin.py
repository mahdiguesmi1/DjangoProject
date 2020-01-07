from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Comment,Category,Product

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Product)