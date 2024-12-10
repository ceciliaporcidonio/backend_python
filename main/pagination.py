# main/pagination.py
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5  # Número de itens por página
    page_size_query_param = 'page_size'  # Permite alterar o tamanho da página via querystring
    max_page_size = 20  # Limite máximo de itens por página

