from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),

    # Local apps
    path('', include('apps.core.urls')),
]
