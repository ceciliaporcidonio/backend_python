from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Relacionamento com o modelo Product
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.product.name}"

