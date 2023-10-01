from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ViewsSales
route = DefaultRouter()

route.register(r'',ViewsSales,basename='Sales')

urlpatterns = [
    path('',include(route.urls))
]