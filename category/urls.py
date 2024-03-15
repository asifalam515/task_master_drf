from django.urls import path, include
from rest_framework.routers import DefaultRouter
from category.models import Category
from category.serializers import CategorySerializers
from category.views import CategoryViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]