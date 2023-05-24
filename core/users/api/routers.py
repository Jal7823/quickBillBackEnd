from django.urls import path,include
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import ViewUsers

router = DefaultRouter()

router.register(r'',ViewUsers,basename='users')

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('',include(router.urls))
    # path('login/', LoginView.as_view()),
]