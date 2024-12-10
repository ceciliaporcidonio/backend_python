from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductViewSetTest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=50.00,
            stock=10
        )
        self.url = '/api/products/'

    def test_get_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


