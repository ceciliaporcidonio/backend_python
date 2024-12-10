# main/viewsets.py
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    """
    ViewSet para gerenciar produtos. Permite operações CRUD.
    """
    queryset = Product.objects.all()  # Obtém todos os produtos do banco
    serializer_class = ProductSerializer  # Usa o serializer previamente criado

