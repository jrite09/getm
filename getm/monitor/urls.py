from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("searching", views.searching, name="searching"),
    path("register", views.register, name="register"),
    path("registered", views.registered, name="registered")
]