from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet)
app_name = 'task1'


urlpatterns = [
    path("", include(router.urls)),
]
