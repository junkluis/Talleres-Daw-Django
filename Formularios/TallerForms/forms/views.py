from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('forms/index.html')
    test = 'prueba'
    context = {
        'text': test,
    }
    return HttpResponse(template.render(context, request))


def agregarPlatillo(request):
    template = loader.get_template('forms/AgregarPlatillo.html')
    test = 'prueba'
    context = {
        'text': test,
    }
    return HttpResponse(template.render(context, request))


def editarPerfil(request):
    return HttpResponse('holis2')



def platilloAgregado(request):
    template = loader.get_template('forms/platillos.html')
    test = 'prueba'
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
    return HttpResponse('holis4')