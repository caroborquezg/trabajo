import email
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar
# Create your views here.

def mostrarfamiliar(request):
    
    familiar1 = Familiar(nombre= "Jorge", apellido = "Bórquez", email = "jorgeborquez@gmail.com" , profesion = "ingeniero")
    
    familiar1.save()

    familiar2 = Familiar(nombre= "Marcela", apellido = "Bórquez", email = "marcelaborquez@gmail.com" , profesion = "Diseñadora")

    familiar2.save()

    familiar3 = Familiar(nombre= "Joaquin", apellido = "Bórquez", email = "joaquinborquez@gmail.com" , profesion = "Arquitecto")

    familiar3.save()
    
    familia = Familiar.objects.all()
    
    return render (request,"templeta1.html,{"familias": familiar})
    
# def estudiantes(self):
    
#     estudiante2 = Estudiante(nombre= "", camada = "11111")
    
#     # curso.save()
    
#     documento = f"El estudiante es : {estudiante2.nombre}, el apellido es: {estudiante2.camada}"
    
#     return HttpResponse(documento)