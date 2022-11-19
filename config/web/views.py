from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleado import FormularioEmpleado

from web.models import Platos
from web.models import Empleados


# Create your views here.

# TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request, 'home.html')


def PlatosVista(request):

    # Rutina para consulta de platos

    platosConsultados = Platos.objects.all()
    print(platosConsultados)

    # esta vista va a utilizar un formulario de django
    # debo craer entonces un objeto de la clase formularioplatps

    formulario = FormularioPlatos()

    # creamos un diccionario para enviar el formulario al html(template)
    data = {
        'formulario': formulario,
        'bandera': False,
        'platos': platosConsultados
    }

    # RECIBIMOS LOS DATOS DEL FORMULARIO
    if request.method == 'POST':
        # deberiamos capturar los datos del formulario
        datosDelFormulario = FormularioPlatos(request.POST)
        # verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            # capturamos la data
            datosPlato = datosDelFormulario.cleaned_data
            # creamos un objeto del tipo MODELO PLATO
            platoNuevo = Platos(
                nombre=datosPlato["nombre"],
                descripcion=datosPlato["descripcion"],
                fotografia=datosPlato["fotografia"],
                precio=datosPlato["precio"],
                tipo=datosPlato["tipo"]
            )
            # Intentamos llevar el objeto platoNuevo a LA BD
            try:
                platoNuevo.save()
                data["bandera"] = True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                print("error", error)
                data["bandera"] = False

            # try:
               # platoNuevo.save()
                # data["bandera"]=True
            # ca

    return render(request, 'menuplatos.html', data)


def EmpleadosVista(request):

    empleadosConsultados = Empleados.objects.all()
    print(empleadosConsultados)

    formulario = FormularioEmpleado()

    data = {
        'formulario': formulario,
        'bandera': False,
        'empleados': empleadosConsultados
    }

    if request.method == 'POST':
        datosDelFormulario = FormularioEmpleado(request.POST)

        if datosDelFormulario.is_valid():

            datosEmpleado = datosDelFormulario.cleaned_data

            empleadoNuevo = Empleados(
                nomempleado=datosEmpleado["nombre"],
                apellidos=datosEmpleado["apellidos"],
                foto=datosEmpleado["foto"],
                cargo=datosEmpleado["cargo"],
                salario=datosEmpleado["salario"]
            )


            try:
                empleadoNuevo.save()
                data["bandera"] = True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                print("error", error)
                data["bandera"] = False

    return render(request, 'empleados.html', data)
