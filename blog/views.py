from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Noticia, Categoria, Corpo
from blog.forms import ComentarioForm, ContatoForm, UsuarioForm, LoginForm, NoticiaForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def home(request):
    todas_noticias = Noticia.objects.all().order_by('-data')
    todos_corpos = Corpo.objects.all()

    context = {'todas_noticias': todas_noticias,
               'todos_corpos': todos_corpos,
               'loginform': LoginForm(),
               'usuarioform': UsuarioForm()}
    
    if request.user.is_authenticated:
        context['usuarioform'] = UsuarioForm(instance=User.objects.get(id=request.user.id))
    
    return render(request, 'index.html', context)


def policia(request):
    loginform = LoginForm()
    usuarioform = UsuarioForm()

    categoria_policia = get_object_or_404(Categoria, nome='Polícia')
    noticias_policia = Noticia.objects.filter(categoria=categoria_policia).order_by('-data')
    context = {'noticias': noticias_policia, 'loginform': loginform, 'usuarioform': usuarioform}
    return render(request, 'policia.html', context)

def esporte(request):
    loginform = LoginForm()
    usuarioform = UsuarioForm()

    categoria_esporte = Categoria.objects.get(nome='Esporte')
    noticias_policia = Noticia.objects.filter(categoria=categoria_esporte)
    context = {'noticias': noticias_policia, 'loginform': loginform, 'usuarioform': usuarioform}
    return render(request, 'esporte.html', context)

def politica(request):
    loginform = LoginForm()
    usuarioform = UsuarioForm()
    try:
        categoria_politica = Categoria.objects.get(nome='Política')
    except Categoria.MultipleObjectsReturned:
        categoria_politica = Categoria.objects.filter(nome='Política').first()

    noticias_politica = Noticia.objects.filter(categoria=categoria_politica).order_by('-data')
    context = {'noticias': noticias_politica, 'loginform': loginform, 'usuarioform': usuarioform}
    return render(request, 'politica.html', context)

def politica_id (request,id_p):
    noticias_politica = Noticia.objects.get(id=id_p)
    context = {'noticias': noticias_politica}
    return render(request, 'politica.html', context)

def contato (request):    
    loginform = LoginForm()
    usuarioform = UsuarioForm()

    if request.method != 'POST':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))
    context = {'form': form, 'loginform': loginform, 'usuarioform': usuarioform}
    return render(request, 'form.html', context)

def destaques (request):
    loginform = LoginForm()
    usuarioform = UsuarioForm()

    categorias = Categoria.objects.all()
    destaques = {}
    for categoria in categorias:
        noticia = Noticia.objects.filter(categoria=categoria).first()
        if noticia:
            destaques[categoria.nome] = noticia

    context = {'destaques': destaques, 'loginform': loginform, 'usuarioform': usuarioform}
    return render(request, 'destaques.html', context)

def detalhes_noticia (request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    comentarios = noticia.comentario_set.all()

    loginform = LoginForm()
    usuarioform = UsuarioForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.noticia = noticia
                comentario.usuario = request.user
                comentario.save()
                return redirect(reverse('detalhes_noticia', kwargs={'noticia_id': noticia_id}))
        else:
            return redirect('login')
    else:
        form = ComentarioForm()
    return render(request, 'detalhes_noticia.html', {'noticia': noticia, 'comentarios': comentarios, 'form': form, 'loginform': loginform, 'usuarioform': usuarioform})


def cadastro_usuario (request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password') != form.data.get('confirmacao'):
                form.add_error('password', 'As senhas devem ser iguais')
            else:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data.get('password'))
                user.save()
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UsuarioForm()

    context = {'usuarioform': form}
    return render(request,'index.html', context)
    #return HttpResponseRedirect(reverse('home'))

def delusuario (request, id):
    user = User.objects.get(id=id)
    user.delete()
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def editar_perfil (request):
    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['username'] = usuario.username
        novo_usuario['password'] = usuario.password
        user = UsuarioForm(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
    return HttpResponseRedirect(reverse('home'))

def login (request):
    if request.method == "POST":
        #fazer login
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            auth_login(request, user = user)
    return HttpResponseRedirect(reverse('home'))

def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))
                    
def cadastronoticia (request):
    loginform = LoginForm()
    usuarioform = UsuarioForm()

    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = NoticiaForm()

    return render(request, 'cadastronoticia.html', {'form': form, 'loginform': loginform, 'usuarioform': usuarioform})

    
