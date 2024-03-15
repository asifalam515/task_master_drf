from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,UserRegistrationApiView,activate,UserLoginApiView,UserLogOutView


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list', UserViewSet, basename='user')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/', activate,name='activate'),
    path('login/', UserLoginApiView.as_view(),name='login'),
    path('logout/', UserLogOutView.as_view(),name='logout'),
]