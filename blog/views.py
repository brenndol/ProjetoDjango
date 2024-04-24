from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Noticia, Categoria, Corpo
from blog.forms import ComentarioForm, ContatoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
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
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'form.html', context)

def destaques (request):
    categorias = Categoria.objects.all()
    destaques = {}
    for categoria in categorias:
        noticia = Noticia.objects.filter(categoria=categoria).first()
        if noticia:
            destaques[categoria.nome] = noticia

    context = {'destaques': destaques}
    return render(request, 'destaques.html', context)

def detalhes_noticia (request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    comentarios = noticia.comentario_set.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.noticia = noticia
                comentario.usuario = request.user
                comentario.save()
                return redirect(reverse('detalhes_noticia', noticia_id=noticia_id))
        else:
            return redirect('login')
    else:
        form = ComentarioForm()
    return render(request, 'detalhes_noticia.html', {'noticia': noticia, 'comentarios': comentarios, 'form': form})


def cadastro_usuario (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'cadastro_usuario.html', {'form': form})
    
def login_usuario (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_usuario (request):
    logout(request)
    return render(request, 'logout.html')