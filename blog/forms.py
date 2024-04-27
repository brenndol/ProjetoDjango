from django import forms
from blog.models import Comentario
from django.contrib.auth.models import User
from django.forms.widgets import*


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['corpo']
        labels = {'corpo': 'Comentário'}
    

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome', widget=forms.TextInput(attrs={'placeholder': 'Seu nome'}))
    telefone = forms.CharField(max_length=20, label='Telefone', required=False, widget=forms.TextInput(attrs={'placeholder': 'Seu telefone'}))
    email = forms.EmailField(max_length=100, label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Seu email'}))
    assunto = forms.CharField(max_length=100, label='Assunto', widget=forms.TextInput(attrs={'placeholder': 'Assunto da mensagem'}))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder': 'Escreva sua mensagem aqui'}))

    class LoginForm(forms.ModelForm):
     class Meta:
        model = User
        fields = ['username','password']
        widgets = {'password': PasswordInput()}                         

        class UsuarioForm(forms.ModelForm):
            class Meta:
                model = User
                fields = ['username','password','email','first_name','last_name']
                widgets = {'email':EmailInput(),'password': PasswordInput()}
        def __init__(self,*args,**kwargs):
                   super().__init__(*args,**kwargs)
                   self.fields['username'].widget.attrs.update({
                       'placeholder':'Usuário',
                       'class': 'form-control my-2 p-2',
                       'autocomplete':'new-password'
                       
                   })
                   self.fields['password'].widget.attrs.update({
                      'placeholder':'Senha',
                       'class': 'form-control my-2 p-2',
                       'autocomplete':'new-password'  
                    })