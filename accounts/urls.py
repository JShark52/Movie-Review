from django.urls import path
from . import views
from .views import UserEditView, PasswordsChangeView, delete_profile
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("editprofile/", UserEditView.as_view(), name="edit_profile"),
    path("deleteprofile/", views.delete_profile, name="delete_profile"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("password/", PasswordsChangeView.as_view(template_name='accounts/change-password.html'))
]