from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import post_list, post_detail

# router = DefaultRouter()
# router.register('post', PostViewset, basename='post')

urlpatterns = [
    path('posts/', post_list),
    path('posts/<int:pk>/', post_detail)
]
