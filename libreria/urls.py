from django.urls import path
from . import views
from django.conf import (settings)
from django.contrib.staticfiles.urls import static

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('registrar', views.formRegistro, name='formRegistro'),
    path('editar', views.formEditar, name='formEditar'),
    path('borrar/<int:id>', views.borrarRegistro, name='borrar'),
    path('personas/editar/<int:id>', views.formEditar, name='editar'),
    
]+ static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
