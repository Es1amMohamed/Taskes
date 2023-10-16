from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("task1/", include("task1.urls", namespace="task1")),
    path("task2/", include("task2.urls", namespace="task2")),
]
