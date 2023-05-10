from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ViewOrderItems,ViewOrders


router = DefaultRouter()

router.register(r'',ViewOrders,basename='orders')
router.register(r'',ViewOrderItems,basename='ordersItem')

urlpatterns = [
    path('',include(router.urls))
]

