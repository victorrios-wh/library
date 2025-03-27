from django import forms
from biblioteca.models import Libro

# class DateInput(forms.DateInput):
#     input_type = 'date'

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada'
        ]

        required = [
            'titulo',
            'autores',
            'editor'
        ]
        
        labels = {
            'titulo': 'Titulo:',
            'autores': 'Autor(es):',
            'editor': 'Editor:',
            'fecha_publicacion': 'Fecha de publicacion:',
            'portada': 'Portada:'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autores': forms.CheckboxSelectMultiple(),
            'editor': forms.Select(attrs={'class':'form-control'}),
            'fecha_publicacion': forms.DateInput()
        }