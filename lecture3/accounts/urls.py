from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts import urls as accounts_urls
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

]
