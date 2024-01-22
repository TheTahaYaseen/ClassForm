from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_view, name="form"),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
]
