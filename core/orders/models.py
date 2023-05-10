from django.db import models
from ..users.models import Users
from ..products.models import Products



class OrderItem(models.Model):
    """Model definition for OrderItem."""

    quantity = models.IntegerField()
    products = models.ManyToManyField(Products)

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return f'{self.id}'


class Orders(models.Model):
    """Model definition for Orders."""

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.FloatField(default=0.0)
    items = models.ManyToManyField(OrderItem)

    class Meta:
        """Meta definition for Orders."""

        verbose_name = 'Orders'
        verbose_name_plural = 'Orderss'

    def __str__(self):
        """Unicode representation of Orders."""
        return f'Cliente: {self.user.username} - Nro. Orden {self.id}'
    




