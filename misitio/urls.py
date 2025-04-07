from django.conf.urls import include, url
from django.contrib import admin
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='home'),
    url(r'^biblioteca/', include('biblioteca.urls', namespace='biblioteca')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
