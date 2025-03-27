from django.conf.urls import url
from biblioteca.views import delete_book, edit_book, list_books, register_book, search_book, \
                        EditBook, DeleteBook, ListBooks, RegisterBook

urlpatterns = [
    # url(r'^$', list_books, name='index'),
    # url(r'^registrar/libro/$', register_book, name='registrar_libro'),
    # url(r'^buscar/libro/$', search_book, name='buscar_libro'),
    # url(r'^editar/libro/(\d+)/$', edit_book, name='editar_libro'),
    # url(r'^eliminar/libro/(\d+)/$', delete_book, name='eliminar_libro'),
    ## DEFINICION CON CLASS BASED VIEWS
    url(r'^$', ListBooks.as_view(), name='index'),
    url(r'^registrar/libro/$', RegisterBook.as_view(), name='registrar_libro'),
    url(r'^buscar/libro/$', search_book, name='buscar_libro'),
    url(r'^editar/libro/(?P<pk>\d+)/$', EditBook.as_view(), name='editar_libro'),
    url(r'^eliminar/libro/(?P<pk>\d+)/$', DeleteBook.as_view(), name='eliminar_libro'),
]