from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
try:
    import json
except ImportError:
    import simplejson

def index(request):
    template = loader.get_template('forms/index.html')
    test = 'prueba'
    context = {
        'text': test,
    }
    return HttpResponse(template.render(context, request))


def agregarPlatillo(request):
    template = loader.get_template('forms/AgregarPlatillo.html')
    context = {}
    return HttpResponse(template.render(context, request))


def editarPerfil(request):
    template = loader.get_template('forms/Editar.html')
    context = {}
    return HttpResponse(template.render(context, request))



def platilloAgregado(request):
    template = loader.get_template('forms/platillos.html')
    if request.method == 'POST':
        nombre = request.POST.get("nombreP","")
        desc = request.POST.get("descripcion", "")
        nutricion = request.POST.get("nutri", "")
        tipo = request.POST.get("tipo", "")
        cuadro = ''
        if(nutricion == 'on'):
            cuadro = 'cuadro deshabilitado'
        else:
            cuadro = 'cuadro Nutricional deshabilitado'
        tipoA = ''
        if(tipo == '1'):
            tipoA = 'Almuerzo'
        elif(tipo == '2'):
            tipoA = 'Desayuno'
        elif(tipo == '3'):
            tipoA = 'Plato a la carta'

    else:
        nombre = 'default value'
    context = {
        'nombreP': nombre,
        'desc': desc,
        'nutricion': cuadro,
        'tipo': tipoA,
    }
    return HttpResponse(template.render(context, request))



def miPerfil(request):
    template = loader.get_template('forms/miPerfil.html')
    if request.method == 'GET':
        nombreCo = request.GET.get("comedorT", "")
        biblio = request.GET.get("bibliografia", "")
        tipo = request.GET.get("tipoL", "")
        ayu = request.GET.get("ayud", "")
        ayudantes = ''
        if (ayu == 'on'):
            ayudantes = 'Se aceptan ayudantes'
        else:
            ayudantes = 'No se aceptan ayudantes'

    context = {
        'nombreCo': nombreCo,
        'biblio': biblio,
        'tipo': tipo,
        'ayu': ayudantes,
    }
    return HttpResponse(template.render(context, request))

#con AJAX
def login(request):
    template = loader.get_template('forms/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bienvenida(request):
    template=loader.get_template('forms/bienvenida.html')
    context = {'email': 'no encontrado'}
    if request.method=='POST':
        context={
            'email':request.POST.get('email',None),
            'password':request.POST.get('pwd',None)
        }
    return render()