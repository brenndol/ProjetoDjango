from django import forms
from blog.models import Comentario

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

        

        
