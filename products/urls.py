

from django.urls import path
from .views import (get_categories, get_products, create_category, create_product, update_product, delete_product,product)


urlpatterns = [
    path('', get_products),
    path('<int:pk>/', product),
    path('create/', create_product),
    path('update/<int:pk>/', update_product),
    path('delete/<int:pk>/', delete_product),
    path('categories/', get_categories),
    path('categories/create/', create_category)
]