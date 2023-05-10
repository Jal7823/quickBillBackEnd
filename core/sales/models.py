from django.db import models
from ..products.models import Products
from ..users.models import Users

class Sales(models.Model):
    """Model definition for Sales."""

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.FloatField(default=0.0)
    products = models.ManyToManyField(Products)     

    class Meta:
        """Meta definition for Sales."""

        verbose_name = 'Sales'
        verbose_name_plural = 'Saless'

    def __str__(self):
        """Unicode representation of Sales."""
        return f'Cliente: {self.user.name} - Pedido Nro. {self.id}' 
