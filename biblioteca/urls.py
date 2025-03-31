from django.conf.urls import url
from biblioteca.views import delete_book, edit_book, list_books, register_book, search_book, \
                        EditBook, DeleteBook, ListBooks, RegisterBook, SearchBook

urlpatterns = [
    url(r'^func/$', list_books, name='index_func'),
    url(r'^func/registrar/libro/$', register_book, name='registrar_libro_func'),
    url(r'^func/buscar/libro/$', search_book, name='buscar_libro_func'),
    url(r'^func/editar/libro/(\d+)/$', edit_book, name='editar_libro_func'),
    url(r'^func/eliminar/libro/(\d+)/$', delete_book, name='eliminar_libro_func'),
    ## DEFINICION CON CLASS BASED VIEWS
    url(r'^cbv/$', ListBooks.as_view(), name='index_cbv'),
    url(r'^cbv/registrar/libro/$', RegisterBook.as_view(), name='registrar_libro_cbv'),
    url(r'^cbv/buscar/libro/$', SearchBook.as_view(), name='buscar_libro_cbv'),
    url(r'^cbv/editar/libro/(?P<pk>\d+)/$', EditBook.as_view(), name='editar_libro_cbv'),
    url(r'^cbv/eliminar/libro/(?P<pk>\d+)/$', DeleteBook.as_view(), name='eliminar_libro_cbv'),
]