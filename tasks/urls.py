from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('create', views.CreateTaskViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]