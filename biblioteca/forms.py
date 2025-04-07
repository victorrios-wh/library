from django import forms
from biblioteca.models import Libro
from django.forms.utils import ErrorList
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join

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

class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self:
            return ''
        return format_html(
            '<div class="errorlist">{}</div>',
            format_html_join('', '<div class="alert alert-danger">{}</div>', ((force_text(e),) for e in self))
        )