from rest_framework import serializers

from .models import Manufacturer, Category, Product, Characteristic, ProductCharacteristic


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class ProductCharacteristicSerializer(serializers.ModelSerializer):
    characteristic = CharacteristicSerializer()

    class Meta:
        model = ProductCharacteristic
        fields = '__all__'

    def create(self, validated_data):
        characteristic_data = validated_data.pop('characteristic')
        characteristic = Characteristic.objects.create(**characteristic_data)
        product_characteristic = ProductCharacteristic.objects.create(characteristic=characteristic, **validated_data)
        return product_characteristic


class ProductSerializer(serializers.ModelSerializer):
    characteristics = ProductCharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
