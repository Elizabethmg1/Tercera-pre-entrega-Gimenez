from django.shortcuts import render
from .models import Hermana,Prima,Tia
from .forms import HermanaFormulario,PrimaFormulario,TiaFormulario
from django.http import HttpResponse

def inicio(request):
    return render(request, "app/inicio.html")

def hermana(request):
    return render(request, "app/hermana.html")

def prima(request):
    return render(request, "app/prima.html")

def tia(request):
    return render(request, "app/tia.html")

def hermanaFormulario(request):
    if request.method == 'POST':
        miFormulario = HermanaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            hermana = Hermana(nombre=informacion['nombre'],edad = informacion['edad'],fechadenacimiento = informacion['fechadenacimiento'])
            hermana.save()

            return render(request,"app/inicio.html")
    else:
        miFormulario = PrimaFormulario()

    return render(request, "app/hermanaFormulario.html", {"miFormulario":miFormulario})

def primaFormulario(request):
    if request.method == 'POST':
        miFormulario = PrimaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            prima = Prima(nombre=informacion['nombre'],edad = informacion['edad'],fechadenacimiento = informacion['fechadenacimiento'])
            prima.save()

            return render(request,"app/inicio.html")
    else:
        miFormulario = PrimaFormulario()

    return render(request, "app/primaFormulario.html", {"miFormulario":miFormulario})

def tiaFormulario(request):
    if request.method == 'POST':
        miFormulario = TiaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            tia = Tia(nombre=informacion['nombre'],edad = informacion['edad'],fechadenacimiento = informacion['fechadenacimiento'])
            tia.save()

            return render(request,"app/inicio.html")
    else:
        miFormulario = TiaFormulario()

    return render(request, "app/tiaFormulario.html", {"miFormulario":miFormulario})

def busquedaHermana(request):
    return render(request,'app/busquedaHermana.html')

def buscarNombreHermana(request):
    nombre = request.GET["nombre"]
    hermanas = Hermana.objects.filter(nombre__icontains=nombre)
    return render(request,'app/resultadosBusquedaHermana.html', {"hermanas":hermanas,"nombre":nombre})

def busquedaPrima(request):
    return render(request,'app/busquedaPrima.html')

def buscarNombrePrima(request):
    nombre = request.GET["nombre"]
    primas = Prima.objects.filter(nombre__icontains=nombre)
    return render(request,'app/resultadosBusquedaPrima.html', {"primas":primas,"nombre":nombre})

def busquedaTia(request):
    return render(request,'app/busquedaTia.html')

def buscarNombreTia(request):
    nombre = request.GET["nombre"]
    tias = Tia.objects.filter(nombre__icontains=nombre)
    return render(request,'app/resultadosBusquedaTia.html', {"tias":tias,"nombre":nombre})
