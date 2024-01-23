from django.urls import path, include

from .views import shop_base_view, product_view, create_view

urlpatterns = [
    path('items', shop_base_view, name='items'),
    path('product/<int:id>', product_view, name='product'),
    path('create/product', create_view, name='create')
]