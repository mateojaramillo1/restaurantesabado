from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleado import FormularioEmpleado

from web.models import Platos


# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def PlatosVista(request):
    
    
    
    #Rutina para consulta de platos
    
    platosConsultados=Platos.objects.all()
    print(platosConsultados)
    
    #esta vista va a utilizar un formulario de django 
    #debo craer entonces un objeto de la clase formularioplatps
    
    formulario=FormularioPlatos()
    
    #creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario,
        'bandera': False,
        'platos': platosConsultados
    }

    #RECIBIMOS LOS DATOS DEL FORMULARIO
    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            #creamos un objeto del tipo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosPlato["nombre"],
                descripcion=datosPlato["descripcion"],
                fotografia=datosPlato["fotografia"],
                precio=datosPlato["precio"],
                tipo=datosPlato["tipo"]
            )
            #Intentamos llevar el objeto platoNuevo a LA BD
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                print("error",error)
                data["bandera"]=False

            
            #try:
               # platoNuevo.save()
                #data["bandera"]=True
            #ca
        
    
    return render(request,'menuplatos.html', data)

def Empleados(request):


    formulario = FormularioEmpleado()

    data={
        'formulario':formulario
    }

    return render(request,'empleados.html', data)


