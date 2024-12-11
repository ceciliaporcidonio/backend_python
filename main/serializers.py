from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Inclui os detalhes do produto no pedido

    class Meta:
        model = Order
        fields = '__all__'

