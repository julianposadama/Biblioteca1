from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self,nombre,apellido):

        self.nombre=nombre

        self.apellido=apellido

def saludo(request): #Primera vista

    p1=Persona("del bibliotecario es: Juan","Posada")

    #nombre="Julian"

    #apellido= "Posada"

    ahora=datetime.datetime.now()
    
    doc_externo=open("C:/Users/USUARIO/Desktop/Proyecto Django/Proyecto1/Proyecto1/plantillas/plantilla 1.html")
   
    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora})
    
    documento= plt.render(ctx)

    return HttpResponse(documento) #Devolvernos respuesta

def despedida(request): #Primera vista

    return HttpResponse("Hasta luego compañeros") #Devolvernos respuesta

def fecha(request):

    fecha_actual=datetime.datetime.now()

    documento=""" <html>
    <body>
    <h2>
    Fecha y hora actual %s
    <h2>
    <body>
    <html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad, agno):

    #edadActual=18
    periodo=agno-2020
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno,edadFutura)

    return  HttpResponse(documento)
