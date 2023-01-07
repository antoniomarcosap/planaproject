from django.urls import path

from . import views

app_name = 'plano'

urlpatterns = [
    path('planlist/', views.ListaPlanos.as_view(),
         name='planlist'),

    path('plandetail/<int:pk>/', views.DetalhePlano.as_view(),
         name='plandetail'),

    path('adicionarplano/', views.AdicionarPlano,
         name='adicionarplano'),

    path('planupdate/<int:pk>/', views.AtualizarPlano,
         name='planupdate'),

    path('removerplano/<int:pk>/', views.RemoverPlano.as_view(),
         name='removeplan'),
]
