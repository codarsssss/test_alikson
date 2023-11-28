from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Manufacturer, Category, Product, ProductCharacteristic
from .serializers import ManufacturerSerializer, CategorySerializer, ProductSerializer, ProductCharacteristicSerializer


class ManufacturerCreateView(generics.CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryFilteredProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        characteristic_filter = self.request.query_params.get('characteristic')
        if characteristic_filter:
            characteristic_name, characteristic_value = characteristic_filter.split(':')
            return Product.objects.filter(
                category_id=category_id,
                characteristics__characteristic__name=characteristic_name,
                characteristics__value=characteristic_value
            )
        return Product.objects.filter(category_id=category_id)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCharacteristicCreateView(generics.CreateAPIView):
    queryset = ProductCharacteristic.objects.all()
    serializer_class = ProductCharacteristicSerializer
