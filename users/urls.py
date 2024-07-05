

from rest_framework import routers
from .views import UserViewSet, FriendViewSet
from django.urls import path, include

# Create a single router instance
router = routers.DefaultRouter()

# Register both UserViewSet and FriendViewSet
router.register(r'users', UserViewSet)
router.register(r'friends', FriendViewSet)

# Define urlpatterns and include router.urls
urlpatterns = [
    path('', include(router.urls)),
]