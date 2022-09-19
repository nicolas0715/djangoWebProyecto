from django.shortcuts import render
from Farmacia.models import Medicamento

# Create your views here.

def laboratorios(request):
    return render(request, "laboratorios.html")

def medicamentos(request):
    if request.method == "POST":
        medic = Medicamento(
            nombreMarca= request.POST["nombreMedicamento"],
            drogaComponente= request.POST["nombreDrogra"], 
            laboratorio= request.POST["nombreLaboratorio"],  
            codigoBarra= request.POST["codigoBarra"]
            )
        medic.save()
        return render(request, "inicio.html")
    return render(request, "medicamentos.html") 

def inicio(request):
    return render(request, "inicio.html")

def sucursales(request):
    return render(request, "sucursales.html")

def ofertas(request):
    return render(request, "ofertas.html")