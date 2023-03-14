from django.urls import path

from . import views

app_name = 'task'

urlpatterns = [
    path('tasklist/', views.TaskList.as_view(),
         name='tasks'),
]

"""
    path('plandetail/<int:pk>/', views.DetalhePlano.as_view(),
         name='plandetail'),

    path('adicionarplano/', views.AdicionarPlano,
         name='adicionarplano'),

    path('planupdate/<int:pk>/', views.AtualizarPlano,
         name='planupdate'),

    path('removerplano/<int:pk>/', views.RemoverPlano.as_view(),
         name='removeplan'),
]
"""
