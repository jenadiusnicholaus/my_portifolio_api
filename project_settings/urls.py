
from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


