from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('policia/', views.policia, name='policia'),
    path('esporte/', views.esporte, name='esporte'),
    path('politica/', views.politica, name='politica'),
    path('destaques/', views.destaques, name='destaques'),
    path('contato/', views.formulario, name='contato'),
    path('noticia/<int:noticia_id>/', views.detalhes_noticia, name='detalhes_noticia'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),



]
