# main/tests/test_serializers.py
from django.test import TestCase
from main.models import Product
from main.serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "description": "A product for testing",
            "price": "99.99",
            "stock": 50
        }
        self.product = Product.objects.create(**self.product_data)

    def test_serialization(self):
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        self.assertEqual(data['name'], self.product_data['name'])
        self.assertEqual(data['description'], self.product_data['description'])
        self.assertEqual(data['price'], self.product_data['price'])
        self.assertEqual(data['stock'], self.product_data['stock'])

    def test_deserialization(self):
        serializer = ProductSerializer(data=self.product_data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.name, self.product_data['name'])
        self.assertEqual(product.description, self.product_data['description'])

