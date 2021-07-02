from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
