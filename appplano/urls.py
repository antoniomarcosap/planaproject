from django.urls import path

from . import views

app_name = 'plano'

urlpatterns = [
    #    path('', views.PlanoView.as_view(), name='planolist'),
    path('create/', views.PlanoCreateView.as_view(), name='planocreate'),
    path('update/<int:pk>/', views.PlanoUpdateView.as_view(), name='planoupdate'),
    #    path('detail/<int:pk>/', views.PlanoDetail.as_view(), name='planodetail'),
    #    path('delete/<int:pk>/', views.PlanoDelete.as_view(), name='planodelete'),
]
