from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ViewsCompany

router = DefaultRouter()

router.register(r'',ViewsCompany,basename='company')

urlpatterns = [
    path('',include(router.urls))
]