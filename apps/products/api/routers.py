from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewBrand, ViewCategory, ViewProducts, ViewProvider

router = DefaultRouter()

router.register(r'', ViewProducts, basename='products')
router.register(r'provider', ViewProvider, basename='provider')
router.register(r'category', ViewCategory, basename='category')
router.register(r'brand', ViewBrand, basename='brand')

urlpatterns = [
    path('', include(router.urls))
]
