from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^editar/$', views.editarPerfil, name='editarPerfil'),
    url(r'^agregar/$', views.agregarPlatillo, name='agregarPlatillo'),
    url(r'^miPerfil/$', views.miPerfil, name='miPerfil'),
    url(r'^platillos/$', views.platilloAgregado, name='platilloAgregado'),
]