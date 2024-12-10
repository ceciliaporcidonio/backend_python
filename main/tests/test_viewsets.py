from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from main.models import Product

class ProductViewSetTest(APITestCase):
    def setUp(self):
        # Dados de exemplo
        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            price=100.00,
            stock=10
        )
        self.list_url = reverse('product-list')  # Rota para listar produtos

    def test_list_products(self):
        """Teste para listar os produtos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        """Teste para criar um produto"""
        data = {
            "name": "New Product",
            "description": "Description for new product",
            "price": "50.00",
            "stock": 100
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().name, "New Product")

    def test_update_product(self):
        """Teste para atualizar um produto"""
        detail_url = reverse('product-detail', kwargs={'pk': self.product.id})
        data = {
            "name": "Updated Product",
            "description": self.product.description,
            "price": "200.00",
            "stock": self.product.stock
        }
        response = self.client.put(detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Product")

    def test_delete_product(self):
        """Teste para deletar um produto"""
        detail_url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

