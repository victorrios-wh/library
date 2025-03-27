from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from biblioteca.models import Libro
from biblioteca.forms import LibroForm

# Create your views here.

class RegisterBook(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'form_libro.html'
    success_url = reverse_lazy('biblioteca:index')

class ListBooks(ListView):
    model = Libro
    template_name = 'listar_libros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['object_list']
        return context

class EditBook(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'form_libro.html'
    success_url = reverse_lazy('biblioteca:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = context['object']
        return context

class DeleteBook(DeleteView):
    model = Libro
    template_name = 'eliminar_libro.html'
    success_url = reverse_lazy('biblioteca:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = context['object']
        return context

def register_book(request):

    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:index')
    else:
        form = LibroForm()

    return render(request, 'form_libro.html', {
        'title': 'Registrar libro',
        'form': form
    })

def list_books(request):
    books = Libro.objects.all()

    return render(request, 'listar_libros.html', {
        'books': books
    })

def edit_book(request, id):
    libro = Libro.objects.filter(id=id).first()

    if libro:
        if request.method == 'GET':
            form = LibroForm(instance=libro)
        else:
            form = LibroForm(request.POST, instance=libro)
            if form.is_valid():
                form.save()
                return redirect('biblioteca:index')
    else:
        return redirect('biblioteca:index')
    
    return render(request, 'form_libro.html', {
        'title': 'Editar libro: {}'.format(libro.titulo),
        'form': form
    })

def delete_book(request, id):
    book = Libro.objects.filter(id=id).first()

    if book:
        if request.method == 'POST':
            book.delete()
            return redirect('biblioteca:index')
    else:
        return redirect('biblioteca:index')
    
    return render(request, 'eliminar_libro.html', {
        'book': book
    })

def search_book(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET.get('q','')
        if not q:
            errors.append('Por favor introduce un termino de busqueda')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres')
        else:
            books = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'form_buscar.html', {
                'query': q,
                'books': books
            })
        
    return render(request, 'form_buscar.html', {
        'errors': errors
    })

# def buscar(request):
#     errors = []
#     contexto = {}
#     if 'q' in request.GET:
#         q = request.GET['q']
#         if not q:
#             errors.append('Por favor introduce un termino de busqueda')
#         elif len(q) > 20:
#             errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres')
#         else:
#             libros = Libro.objects.filter(titulo__icontains=q)
#             contexto.update({
#                 'libros':libros,
#                 'query': q
#             })
#             return render(request, 'listar_libros.html', contexto)
    
#     contexto.update({
#         'errors': errors
#     })
#     return  render(request, 'formulario_buscar.html', contexto)