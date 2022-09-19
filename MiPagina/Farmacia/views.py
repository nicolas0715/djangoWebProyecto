from django.shortcuts import render
from Farmacia.models import Medicamento
from django.http import HttpResponse

#from Farmacia.forms import form_medicamento

# Create your views here.

def laboratorios(request):
    return render(request, "laboratorios.html")

def medicamentos(request):
    if request.method == "POST":
        medic = Medicamento(
            nombreMarca= request.POST["nombreMedicamento"],
            drogaComponente= request.POST["nombreDroga"], 
            laboratorio= request.POST["nombreLaboratorio"],  
            codigoBarra= request.POST["codigoBarra"]
            )
        medic.save()
        return render(request, "inicio.html")
    return render(request, "medicamentos.html") 

#def api_medicamento(request):
#    if request.method == "POST":
#        formulario = form_medicamento(request.POST)
#        if formulario.is_valid():
#            informacion = formulario.cleaned_data
#            medic = Medicamento(
#                nombreMarca= informacion["nombreMedicamento"],
#                drogaComponente= informacion["nombreDroga"], 
#                laboratorio= informacion["nombreLaboratorio"],  
#                codigoBarra= informacion["codigoBarra"]
#                )
#            medic.save()
#            return render(request, "api_medicamento.html")
#    else:
#        formulario = form_medicamento()
#    return render(request, "api_medicamento.html", {"formulario": formulario})

def buscar_medicamento(request):
    if request.GET["nombreMedicamento"]:
        nombre= request.GET["nombreMedicamento"]
        medicamentos= Medicamento.object.filter(
            nombreMarca__icontains = nombre
        )
        return render(request, "medicamentos.html", {"medicamendo": medicamentos})
    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request, "inicio.html")

def sucursales(request):
    return render(request, "sucursales.html")

def ofertas(request):
    return render(request, "ofertas.html")