from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def getInfoUser(request):
    usuario = request.user
    s = "Usuario actual: " + str(usuario)
    return render(request, "aplicacion12/index.html", {'user':s})


def operacion1(request):
    return HttpResponse("<h3>Esta operación es libre ...</h3>")

@login_required
def operacion2(request):
    s = "Esta operación NO es libre, hay que autenticarse, si entras es que estas autenticado!"
    return HttpResponse("<h3>"+s+"</h3>")
