from django.shortcuts import render
from blog.models import Noticia
from blog.models import Categoria
# Create your views here.
def home (request):
    noticia = Noticia.objects.order_by('id')
    context = {'notica': noticia}
    return render(request,'index.html', context)

def policia (request):
    noticias = Noticia.objects.order_by('id')
    context = {'categorias': noticias}
    return render(request, 'policia.html', context)

def esporte (request):
    noticias = Noticia.objects.order_by('id')
    context = {'categorias': noticias}
    return render(request, 'esporte.html', context)