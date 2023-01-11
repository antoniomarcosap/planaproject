from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('account/register/', views.RegisterView, name='register'),
    path('account/profile/edit', views.UserEditView, name='editprofile'),

    #    path('login/', views.LoginView, name='login'),

    #    path('logout/', views.LogouView, name='logout'),
]
