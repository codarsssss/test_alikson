from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Manufacturer, Category, Product, ProductCharacteristic, Characteristic


class ProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Создаем Manufacturer и Category
        self.manufacturer = Manufacturer.objects.create(name='Test Manufacturer')
        self.category = Category.objects.create(name='Test Category')

        # Создаем Product
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            manufacturer=self.manufacturer
        )

        # Создаем Characteristic
        self.characteristic = Characteristic.objects.create(
            name='Test Characteristic',
            value='Test Value'
        )

        # Создаем ProductCharacteristic
        self.product_characteristic = ProductCharacteristic.objects.create(
            product=self.product,
            characteristic=self.characteristic,
            value='Test Characteristic Value'
        )

    def test_create_manufacturer(self):
        url = reverse('manufacturer-create')
        data = {'name': 'New Manufacturer'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Manufacturer.objects.count(), 2)

    def test_create_category(self):
        url = reverse('category-create')
        data = {'name': 'New Category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_create_product(self):
        url = reverse('product-create')
        data = {
            'name': 'New Product',
            'category': self.category.id,
            'manufacturer': self.manufacturer.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_get_product_list(self):
        url = reverse('product-list', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product_characteristic(self):
        url = reverse('product-characteristic-create')
        data = {
            'product': self.product.id,
            'characteristic': {
                'name': 'New Characteristic',
                'value': 'New Characteristic Value'
            },
            'value': 'New Characteristic Value'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductCharacteristic.objects.count(), 2)

    def test_filter_products_by_characteristic(self):
        url = reverse('category-filtered-products', args=[self.category.id])
        characteristic_filter = f"{self.characteristic.name}:{self.product_characteristic.value}"
        response = self.client.get(url, {'characteristic': characteristic_filter})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
