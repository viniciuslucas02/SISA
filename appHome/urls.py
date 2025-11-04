# Importe a função path do módulo django.urls para definir os padrões de URL
from django.urls import path

# Importe o módulo views do diretório atual
from . import views

urlpatterns = [
    # Define a view a ser chamada quando a URL é acessada
    path('', views.appHome, name='appHome'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]