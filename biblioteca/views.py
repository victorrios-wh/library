from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from biblioteca.models import Libro
from biblioteca.forms import LibroForm, DivErrorList

# Create your views here.

class RegisterBook(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'form_libro.html'
    success_url = reverse_lazy('biblioteca:index_cbv')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Libro registrado exitosamente')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            "initial": self.get_initial(),
            "prefix": self.get_prefix(),
        }
        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "data": self.request.POST,
                    "files": self.request.FILES,
                    "error_class": DivErrorList
                }
            )
        return kwargs

class ListBooks(ListView):
    model = Libro
    template_name = 'listar_libros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origin'] = 'cbv'
        context['books'] = context['object_list']
        return context

class EditBook(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'form_libro.html'
    success_url = reverse_lazy('biblioteca:index_cbv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = context['object']
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Libro editado exitosamente')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"instance": self.object})
        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "error_class": DivErrorList
                }
            )
        return kwargs

class DeleteBook(DeleteView):
    model = Libro
    template_name = 'eliminar_libro.html'
    success_url = reverse_lazy('biblioteca:index_cbv')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origin'] = 'cbv'
        context['book'] = context['object']
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, 'Libro eliminado exitosamente')
        return HttpResponseRedirect(success_url)

class SearchBook(ListView):
    template_name = 'form_buscar.html'
    errors = []
    q = ''

    def get_queryset(self):
        self.errors = []
        if 'q' in self.request.GET:
            q = self.request.GET.get('q','')
            if not q:
                self.errors.append('Por favor introduce un termino de busqueda')
            elif len(q) > 20:
                self.errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres')
            else:
                return Libro.objects.filter(titulo__icontains=self.query())
    
    def query(self):
        self.q = self.request.GET.get('q')
        return self.q
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.q
        context['origin'] = 'cbv'
        context['books'] = context['object_list']
        context['errors'] = self.errors
        return context

def register_book(request):

    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, error_class=DivErrorList)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro registrado exitosamente')
            return redirect('biblioteca:index_func')
    else:
        form = LibroForm()

    return render(request, 'form_libro.html', {
        'title': 'Registrar libro',
        'form': form
    })

def list_books(request):
    books = Libro.objects.all()

    return render(request, 'listar_libros.html', {
        'origin': 'func',
        'books': books
    })

def edit_book(request, id):
    libro = Libro.objects.filter(id=id).first()

    if libro:
        if request.method == 'GET':
            form = LibroForm(instance=libro)
        else:
            form = LibroForm(request.POST, request.FILES, instance=libro, error_class=DivErrorList)
            if form.is_valid():
                form.save()
                messages.success(request, 'Libro editado exitosamente')
                return redirect('biblioteca:index_func')
    else:
        return redirect('biblioteca:index_func')
    
    return render(request, 'form_libro.html', {
        'title': 'Editar libro: {}'.format(libro.titulo),
        'form': form
    })

def delete_book(request, id):
    book = Libro.objects.filter(id=id).first()

    if book:
        if request.method == 'POST':
            book.delete()
            messages.success(request, 'Libro eliminado exitosamente')
            return redirect('biblioteca:index_func')
    else:
        return redirect('biblioteca:index_func')
    
    return render(request, 'eliminar_libro.html', {
        'origin': 'func',
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
                'origin': 'func',
                'books': books
            })
        
    return render(request, 'form_buscar.html', {
        'origin': 'func',
        'errors': errors
    })
