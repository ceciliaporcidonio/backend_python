from rest_framework.test import APITestCase
from rest_framework import status
from main.models import Product

class PaginationTest(APITestCase):
    def setUp(self):
        # Criação de 25 produtos para testar a paginação
        for i in range(25):
            Product.objects.create(
                name=f"Product {i + 1}",
                description=f"Description {i + 1}",
                price=100.00 + i,
                stock=10 + i
            )
        self.url = '/api/products/'

    def test_pagination_default_page_size(self):
        """Teste da paginação com tamanho padrão"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)  # PAGE_SIZE configurado como 10

    def test_pagination_custom_page_size(self):
        """Teste da paginação com tamanho customizado"""
        response = self.client.get(self.url, {'page_size': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

    def test_pagination_second_page(self):
        """Teste da navegação para a segunda página"""
        response = self.client.get(self.url, {'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

