from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts import urls as accounts_urls
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('profile-redirect/', views.profile_redirect, name='profile_redirect'),

]
