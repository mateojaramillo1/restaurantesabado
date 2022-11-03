from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleado import FormularioEmpleado


# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def Platos(request):
    
    #esta vista va a utilizar un formulario de django 
    #debo craer entonces un objeto de la clase formularioplatps
    
    formulario=FormularioPlatos()
    
    #creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario
    }
    
    return render(request,'menuplatos.html', data)

def Empleados(request):


    formulario = FormularioEmpleado()

    data={
        'formulario':formulario
    }

    return render(request,'empleados.html', data)


