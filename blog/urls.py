from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('policia/', views.policia, name='policia'),
    path('esporte/', views.esporte, name='esporte'),
    path('politica/', views.politica, name='politica'),
    path('destaques/', views.destaques, name='destaques'),
    path('contato/', views.contato, name='contato'),
    path('noticia/<int:noticia_id>/', views.detalhes_noticia, name='detalhes_noticia'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('delusuario/<id>', views.delusuario, name='delusuario'),
    path('cadastronoticia/', views.cadastronoticia, name='cadastronoticia')
]
