from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('register/', views.RegisterView, name='register'),

    path('login/', views.LoginView, name='login'),

    path('logout/', views.LogoutView, name='logout'),
]
