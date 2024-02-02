from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from aplicacion10.models import Persona
from aplicacion10.resources import PersonResource

import random, csv

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, A5, A3, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm, cm

# Create your views here.
def texto(n=10):    
    return "".join([chr(random.randint(65,65+25)) for i in range(n)])
    

def generar(request):
    # Generar aleatoriamente una serie de registros:
   
    for i in range(10):
        p = Persona()
        p.nombre = texto(5)
        p.apellido1 = texto(5)
        p.apellido2 = texto(5)
        p.telefono = "12345678"
        p.dni = "5100000" + str(i)
        p.email = "webmaster@hotmail"+str(i)+".com"        
        p.save()
               
    return HttpResponse("<h3>Se han generado 10 registros ...</h3>")

def ver(request):
    L=Persona.objects.all()
    return render(request, 'listado.html', {'registros':L})



def exportarpdf(request):
    response = HttpResponse(content_type='application/pdf')    
    response['Content-Disposition'] = 'attachment; filename=personas.pdf'  
    c = canvas.Canvas(response, pagesize=landscape(A4))
    height, width = A4    # Esta apaisada, intercambio.

    # Pasa los datos del modelo a una lista de listas.
    L = Persona.objects.all()
    data = [Persona.getCabeceras()]
    for i in L:
        data.append(i.to_list())

    alturaTabla = len(data) * 18

    table = Table(data)
    table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                    ("ALIGN", (0,0), (-1,-1), "CENTER"),
                    ('GRID', (0,0), (-1,-1), 1, colors.black)])
       
    table.wrapOn(c, width, height)
    inicioTb = round((height/cm-alturaTabla/cm),0)-2    
    table.drawOn(c, 2*cm, inicioTb*cm) 
         
    styles = getSampleStyleSheet()    
    ptext = "LISTADO DE PERSONAS"
    p = Paragraph(ptext, style=styles["Normal"])   
    p.wrapOn(c, 50*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
    p.drawOn(c, 2*cm, 20*cm)    # position of text / where to draw
    
    c.showPage()
    c.save()
    return response


def exportarcsv(request):   
    # Crea un objeto HttpResponse con las cabeceras CSV correctas:
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=personas.csv'

    # Accede al modelo:
    L=Persona.objects.all()

    #Crear un writer para CSV utilizando el objeto Response:    
    writer = csv.writer(response)
    writer.writerow(Persona.getCabeceras())
    for i in L:
        fila = [i.nombre, i.apellido1, i.apellido2, i.dni, i.telefono, i.email]
        writer.writerow(fila)

    return response


def exportarcsv2(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=personas2.csv'
    return response


def exportarjson(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="personas.json'
    return response


def exportarexcel(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="personas.xls"'
    return response

def exportarxml(request):      
    L=Persona.objects.all()
    return render(request, 'personas.xml', {'registros':L},content_type="text/xml")