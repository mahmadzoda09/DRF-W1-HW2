from django.urls import path
from .views import category , category_detail , products , product_detail

urlpatterns = [
    path('category/' , category),
    path('category/<int:pk>' , category_detail),
    path('products/' , products),
    path('products/<int:pk>' , product_detail)
]
