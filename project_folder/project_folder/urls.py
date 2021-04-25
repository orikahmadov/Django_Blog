from django.contrib import admin
from django.urls import path
from app import views as app_views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.index, name =  "index"),
    path('register/', users_views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name="login"),
    path('profile/<int:profile_id>/', users_views.profile, name="profile"),
]
