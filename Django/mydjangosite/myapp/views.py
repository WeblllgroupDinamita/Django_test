from django.shortcuts import render, redirect
from .models import datos
from .forms import DatoForm

# Create your views here
#def index(request):
#    return render(request, "myapp/index.html", {})

#CRUD FUNCTIONS
def login(request):
    return render(request, 'login.html')

def mostrar(request):
    data = datos.objects.all()
    return render(request, 'index.html', {'show_data': data})

def agregar_dato(request):
    formulario = DatoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('mostrar')
    return render(request, 'agregar.html', {'formulario': formulario})

def modificar_dato(request, id):
    data = datos.objects.get(id=id)
    formulario = DatoForm(request.POST or None, request.FILES or None, instance=data)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('mostrar')
    return render(request, 'modificar.html', {'formulario': formulario})

def eliminar_dato(request, id):
    data = datos.objects.get(id=id)
    data.delete()
    return redirect('mostrar')
