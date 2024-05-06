from django import forms
from blog.models import Comentario, Categoria, Noticia, Corpo, Imagem, Contato
from django.forms.widgets import *
from django.contrib.auth.models import User

class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['corpo']
        labels = {'corpo': 'Comentário'}
    

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','assunto','mensagem']
        widgets = {'nome': TextInput(), 'email': TextInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':'Nome','class':'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email','class':'form-control'})
        self.fields['assunto'].widget.attrs.update({'placeholder':'Assunto','class':'form-control'})
        self.fields['mensagem'].widget.attrs.update({'placeholder':'Escreva sua mensagem','class':'form-control'})


class LoginForm (forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'password']
        widgets = {'password': PasswordInput()}    
    def __init__ (self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Usuário','class': 'form-control my-2 p-2'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Senha','class': 'form-control my-2 p-2'})
    
class UsuarioForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'email': EmailInput(), 'password': PasswordInput()}
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True',
            'placeholder': 'Nome de Usuário',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })

        self.fields['password'].widget.attrs.update({'required':'True',
            'placeholder': 'Senha',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })
        self.fields['email'].widget.attrs.update({'required':'True',
            'placeholder': 'Email',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })
        self.fields['first_name'].widget.attrs.update({'required':'True',
            'placeholder': 'Nome',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })
        self.fields['last_name'].widget.attrs.update({'required':'True',
            'placeholder': 'Sobrenome',
            'class': 'form-control my-2 p-2',
            'autocomplete': 'new-password'
        })

class CategoriaForm (forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {'nome': TextInput()}
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':'Nome da categoria', 'class':'form-control'})

class NoticiaForm (forms.ModelForm):
    corpo = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Corpo da Notícia','class':'form-control'}))
    imagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Nome do Arquivo da Imagem','class':'form-control'}))

    class Meta:
        model = Noticia
        fields = ['nome','categoria']
        widgets = {'nome': TextInput()}
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':'Nome','class':'form-control'})
        self.fields['categoria'].widget.attrs.update({'placeholder':'Categoria','class':'form-control'})

class CorpoForm (forms.ModelForm):
    class Meta:
        model = Corpo
        fields = ['corpo']
        widgets = {'corpo': forms.Textarea(attrs={'placeholder': 'Conteúdo', 'class': 'form-control'})}

class ImagemForm (forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['nome']
        widgets = {'nome': TextInput()}
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':'Nome do Arquivo da Imagem','class':'form-control'})
