from rest_framework.routers import DefaultRouter
from core.views import ImageViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]