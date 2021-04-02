from django.urls import path
from .views import register, Login, User_Profile, View_Profile, Retry_Login

app_name = "Profile"
urlpatterns = [
    path('register', register, name="Register"),
    path('login', Login, name="Login"),
    path('profile', User_Profile, name="Profile"),
    path('profile/<slug>', View_Profile, name="View"),
    path('retry/',Retry_Login,name="Retry"),
    ]
