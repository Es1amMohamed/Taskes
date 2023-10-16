from . import views
from django.urls import include, path
from .views import *

app_name = "task2"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
]
