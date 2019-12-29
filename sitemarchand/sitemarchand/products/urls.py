from django.urls import path

from . import views
urlpatterns = [
    path('api/product/', views.ProductListCreate.as_view() ),
    path('api/category/', views.CategoryListCreate.as_view() ),
    path('api/comment/', views.CommentListCreate.as_view() ),
    path('api/comments/',views.AllCommentsListCreate.as_view() ),

]
