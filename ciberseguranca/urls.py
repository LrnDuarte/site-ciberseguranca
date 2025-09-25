from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui todas as URLs do app 'site_escola'.
    # A rota '' (vazia) significa que as URLs de site_escola (como '' e 'quiz/')
    # serão acessadas a partir da raiz do site.
    path('', include('site_escola.urls')),
]
