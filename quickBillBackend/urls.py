from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import send_order

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #apps
    path('products/',include('core.products.api.routers')),
    # path('sales',include('core.sales.api.routers')),
    path('users/',include('core.users.api.routers')),
    path('orders/',include('core.orders.api.routers')),
    path('company/',include('core.company.api.routers')),
    path('sales/',include('core.sales.api.routers')),

    #token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #send email
    path('sendOrder/',send_order,name='sendOrder')



]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
