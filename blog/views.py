from django.shortcuts import render, get_object_or_404
from blog.models import Noticia, Categoria, Corpo
from blog.forms import NoticiaForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    todas_noticias = Noticia.objects.all().order_by('-data')
    todas_corpos = Corpo.objects.all()

    context = {'todas_noticias': todas_noticias,
               'todos_corpos': todas_corpos}
    
    return render(request, 'index.html', context)


def policia(request):
    categoria_policia = get_object_or_404(Categoria, nome='Polícia')
    noticias_policia = Noticia.objects.filter(categoria=categoria_policia).order_by('-data')
    context = {'noticias': noticias_policia}
    return render(request, 'policia.html', context)

def esporte(request):
    categoria_esporte = Categoria.objects.get(nome='Esporte')
    noticias_policia = Noticia.objects.filter(categoria=categoria_esporte)
    context = {'noticias': noticias_policia}
    return render(request, 'esporte.html', context)

def politica(request):
    try:
        categoria_politica = Categoria.objects.get(nome='Política')
    except Categoria.MultipleObjectsReturned:
        categoria_politica = Categoria.objects.filter(nome='Política').first()

    noticias_politica = Noticia.objects.filter(categoria=categoria_politica).order_by('-data')
    context = {'noticias': noticias_politica}
    return render(request, 'politica.html', context)


def politica_id (request,id_p):
    noticias_politica = Noticia.objects.get(id=id_p)
    context = {'noticias': noticias_politica}
    return render(request, 'politica.html', context)

def formulario (request):
    if request.method != 'POST':
        form = NoticiaForm()
    else:
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'form.html', context)