from django.db import models
from ..products.models import Products
from ..users.models import Users


class Sales(models.Model):
    """Model definition for Sales."""

    PAYMENT_STATUS = [
        ('Impago', 'Impago'),
        ('En Proceso', 'En Proceso'),
        ('Verificado', 'Verificado'),
    ]

    ORDER_STATUS = [
        ('Sin Iniciar','Sin Iniciar'),
        ('En preparacion','En preparacion'),
        ('Pendiente por confirmacion de pago','Pendiente por confirmacion de pago'),
        ('Despachado','Despachado'),
    ]

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0.0)
    products = models.ManyToManyField(Products)
    order_status = models.CharField('Estado de la orden', choices=ORDER_STATUS, max_length=200, default='Impago')
    payment_status = models.CharField('Estado del pago', choices=PAYMENT_STATUS, max_length=200, default='Sin Iniciar')
    date = models.DateField(auto_now_add=True)

    class Meta:
        """Meta definition for Sales."""

        verbose_name = 'Sales'
        verbose_name_plural = 'Saless'

    def __str__(self):
        """Unicode representation of Sales."""
        return f'Cliente: {self.user.name} - Pedido Nro. {self.id} '
