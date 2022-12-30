from django.urls import path

from . import views

app_name = 'plano'

urlpatterns = [
    #    path('', views.IndexView.as_view(), name='index'),
    #    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    #    path('planslist/', views.PlanslistView.as_view(), name='planslist'),
    path('create/', views.PlanoCreateView.as_view(), name='planocreate'),
    path('update/<int:pk>/', views.PlanoUpdateView.as_view(), name='planoupdate'),
    #    path('detail/<int:pk>/', views.PlanoDetail.as_view(), name='planodetail'),
    #    path('delete/<int:pk>/', views.PlanoDelete.as_view(), name='planodelete'),
]
