from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Characteristic(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, related_name='characteristics', on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
