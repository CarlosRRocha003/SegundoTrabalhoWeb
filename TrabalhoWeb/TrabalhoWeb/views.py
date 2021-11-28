from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from TrabalhoWeb.models import Candidato, Usuario, Empresa
from TrabalhoWeb.forms import CandidatoModel2Form, UsuarioModel2Form, EmpresaModel2Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.
def home(request):
    return render(request, 'TrabalhoWeb/home.html')

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
        formulario.__getattribute__('username')
        if formulario.is_valid(): 
            formulario.save() 
            LoginView.as_view(template_name='TrabalhoWeb/registro/login2.html')
            return redirect('sec-home') 
    else: 
        formulario = UserCreationForm() 
    context = {'form': formulario} 
    return render(request, 'TrabalhoWeb/registro/registro.html', context)

def tipoConta(request): 
    if request.method == 'POST': 
        tipo = request.POST['tipo'] 
        if tipo == 'CANDIDATO':  
            return redirect('cria-candidato') 
        else:
            return redirect('cria-empresa')
    else: 
        return render(request, 'TrabalhoWeb/registro/tipoConta.html')
    context = {'form': formulario} 
    return render(request, 'TrabalhoWeb/registro/registro.html', context)

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

class EmpresaView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': EmpresaModel2Form, }
        return render(request,"TrabalhoWeb/criaEmpresa.html", context)

    def post(self, request, *args, **kwargs):
        formulario = EmpresaModel2Form(request.POST)
        if formulario.is_valid():
            empresa = formulario.save()
            empresa.save()
            return HttpResponseRedirect(reverse_lazy("lista-empresa"))
        else:
            context = {'empresa': formulario, }
            return render(request, 'TrabalhoWeb/atualizaEmpresa.html', context)

class CandidatoListView(View):
 def get(self, request, *args, **kwargs):
    candidato = Candidato.objects.all()
    context = { 'candidato': candidato, }
    return render(request,'TrabalhoWeb/listaCandidato.html', context)

class EmpresaListView(View):
 def get(self, request, *args, **kwargs):
    empresa = Empresa.objects.all()
    context = { 'empresa': empresa, }
    return render(request,'TrabalhoWeb/listaEmpresa.html', context)
