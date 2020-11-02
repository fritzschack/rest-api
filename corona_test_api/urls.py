from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .api.views import UserViewSet, GroupViewSet, TestLocationViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'testlocations', TestLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]