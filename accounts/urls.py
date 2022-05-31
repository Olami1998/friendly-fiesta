from django.urls import path
from .views import signup, login

urlpatterns = [
    path("signup/", signup), #section a
    path("login/",login), #section b
]
