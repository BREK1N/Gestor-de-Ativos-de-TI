from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
]
