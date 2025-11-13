from django.urls import path
from . import views

urlpatterns = [
    # URL raiz do app (ex: /equipamentos/) vai mostrar a lista
    path('', views.lista_equipamentos, name='lista_equipamentos'),
    path('cadastrar/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    # URL para detalhes (ex: /equipamentos/1/)
    path('<int:pk>/', views.detalhe_equipamento, name='detalhe_equipamento'),
    path('<int:pk>/editar/', views.editar_equipamento, name='editar_equipamento'),
    path('<int:pk>/deletar/', views.deletar_equipamento, name='deletar_equipamento'),
]
