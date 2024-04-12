from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('policia/', views.policia, name='policia'),
    path('esporte/', views.esporte, name='esporte'),
    path('politica/', views.politica, name='politica'),
    path('formulario/', views.formulario, name='formulario')

]
