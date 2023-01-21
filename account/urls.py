from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('account/register/', views.RegisterView, name='register'),
    path('account/login/', views.LoginView, name='login'),
    path('account/profile/edit/', views.UserEditView, name='editprofile'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/dashboard/', views.DashboardView, name='dashboard'),

    path('account/password_change/',
         views.PasswordChangeView, name='password_change'),

]
