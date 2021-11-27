from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from TrabalhoWeb.models import Candidato, Usuario, Empresa
from TrabalhoWeb.forms import CandidatoModel2Form, UsuarioModel2Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'TrabalhoWeb/hello.html')

def loginHome(request):
    return render(request, 'TrabalhoWeb/login.html')

def paginaSecreta(request):
    return render(request, 'TrabalhoWeb/paginaSecreta.html')

def SegundaPagina(request):
    return render(request, 'TrabalhoWeb/criaCandidato.html')

def homeSec(request): 
    return render(request, "TrabalhoWeb/registro/homeSec.html")

def registro(request): 
    if request.method == 'POST': 
        formulario = UserCreationForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save() 
            return redirect('sec-home') 
    else: 
        formulario = UserCreationForm() 
    context = {'form': formulario} 
    return render(request, 'TrabalhoWeb/registro/registro.html', context)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'TrabalhoWeb/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            type = request.GET['tipo']
            if type == "CANDIDATO":
                context = { 'formulario': CandidatoModel2Form, }
                return render(request,"TrabalhoWeb/criaCanditado.html", context)
            else:
                return render(request,"TrabalhoWeb/hello.html")
        else:
            context = { 'formulario': UsuarioModel2Form, }
            return render(request,"TrabalhoWeb/criaUsuario.html", context)

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': UsuarioModel2Form, }
        return render(request,"TrabalhoWeb/criaUsuario.html", context)

    def post(self, request, *args, **kwargs):
        formulario = UsuarioModel2Form(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy("lista-usuario"))
        else:
            context = {'usuario': formulario, }
            return render(request, 'TrabalhoWeb/atualizaUsuario.html', context)

class CandidatoView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': CandidatoModel2Form, }
        return render(request,"TrabalhoWeb/criaCandidato.html", context)

    def post(self, request, *args, **kwargs):
        formulario = CandidatoModel2Form(request.POST)
        if formulario.is_valid():
            candidato = formulario.save()
            candidato.save()
            return HttpResponseRedirect(reverse_lazy("lista-candidato"))
        else:
            context = {'candidato': formulario, }
            return render(request, 'TrabalhoWeb/atualizaCandidato.html', context)

class CandidatoListView(View):
 def get(self, request, *args, **kwargs):
    candidato = Candidato.objects.all()
    context = { 'candidato': candidato, }
    return render(request,'TrabalhoWeb/listaCandidato.html', context)




