from django.urls import path
from .views import (
    ManufacturerCreateView,
    CategoryCreateView,
    ProductListView,
    ProductDetailView,
    CategoryFilteredProductListView,
    ProductCreateView,
    ProductCharacteristicCreateView
)

urlpatterns = [
    path('manufacturers/', ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path('categories/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:category_id>/products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/<int:category_id>/filtered-products/', CategoryFilteredProductListView.as_view(), name='category-filtered-products'),
    path('product-characteristics/', ProductCharacteristicCreateView.as_view(), name='product-characteristic-create'),
    path('products/', ProductCreateView.as_view(), name='product-create'),
]
