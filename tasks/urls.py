from rest_framework import routers
from .viewset_api import TaskViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]