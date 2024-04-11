from django.shortcuts import render
from blog.models import Noticia, Categoria

def home(request):
    # Recupera todas as notícias de cada categoria
    todas_noticias_policia = Noticia.objects.filter(categoria__nome='Polícia')
    todas_noticias_esporte = Noticia.objects.filter(categoria__nome='Esporte')
    todas_noticias_politica = Noticia.objects.filter(categoria__nome='Política')

    context = {
        'todas_noticias_policia': todas_noticias_policia,
        'todas_noticias_esporte': todas_noticias_esporte,
        'todas_noticias_politica': todas_noticias_politica,
    }

    return render(request, 'index.html', context)


def policia(request):
    categoria_policia = Categoria.objects.get(nome='Polícia')
    noticias_policia = Noticia.objects.filter(categoria=categoria_policia)
    context = {'noticias': noticias_policia}
    return render(request, 'policia.html', context)

def esporte(request):
    categoria_esporte = Categoria.objects.get(nome='Esporte')
    noticias_policia = Noticia.objects.filter(categoria=categoria_esporte)
    context = {'noticias': noticias_policia}
    return render(request, 'esporte.html', context)

def politica (request):
    categoria_politica = Categoria.objects.get(nome='Política')
    noticias_politica = Noticia.objects.filter(categoria=categoria_politica)
    context = {'noticias': noticias_politica}
    return render(request, 'politica.html', context)