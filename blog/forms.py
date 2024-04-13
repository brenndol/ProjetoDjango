from django import forms
from blog.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['nome', 'categoria']
        labels = {'nome': 'Digite o título',
                  'categoria': 'Categoria',
                  }
        

        
