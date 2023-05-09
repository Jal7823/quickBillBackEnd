from django.contrib import admin
from .models import Brand,Category,Products,Provider

admin.site.register([Brand,Category,Provider,Products])
