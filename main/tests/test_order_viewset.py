from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from main.models import Order

class OrderViewSetTest(APITestCase):
    def setUp(self):
        # Cria um usuário para autenticação
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

        # Gera o token de acesso
        response = self.client.post('/api/token/', {"username": "testuser", "password": "testpassword"})
        self.access_token = response.data["access"]

        # Configura o cabeçalho de autenticação
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Cria um pedido para teste
        self.order = Order.objects.create(
            customer="John Doe",
            product="Test Product",
            quantity=2
        )
        self.list_url = "/api/orders/"

    def test_list_orders(self):
        """Teste para listar pedidos autenticado"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order_unauthenticated(self):
        """Teste para criar pedido sem autenticação"""
        self.client.credentials()  # Remove o cabeçalho de autenticação
        data = {
            "customer": "Jane Doe",
            "product": "Another Product",
            "quantity": 1
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

