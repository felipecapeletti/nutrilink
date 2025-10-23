from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import health, ItemViewSet, profile

router = DefaultRouter()
router.register(r"items", ItemViewSet, basename="item")

urlpatterns = [
    path("health/", health),
    path("profile/", profile),
    path("", include(router.urls)),
]
