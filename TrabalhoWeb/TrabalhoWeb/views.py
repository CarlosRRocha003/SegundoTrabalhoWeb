from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from TrabalhoWeb.models import Candidato, Usuario, Empresa
from TrabalhoWeb.forms import CandidatoModel2Form, UsuarioModel2Form, EmpresaModel2Form
from django.contrib.auth import authenticate, login
from TrabalhoWeb.admin import UserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.
def home(request):
    try:
        print("oi")
        if request.user.tipo == "EMPRESA":
            return render(request, 'TrabalhoWeb/registro/homeEmpresa.html')
        else:
            return render(request, 'TrabalhoWeb/registro/homeCandidato.html')
    except:
        return redirect('sec-login')

def loginHome(request):
    return render(request, 'TrabalhoWeb/login.html')

def SegundaPagina(request):
    return render(request, 'TrabalhoWeb/criaCandidato.html')

def homeSec(request): 
    return render(request, "TrabalhoWeb/registro/homeSec.html")

def verCandidato(request):
    user = request.user
    try:
        candidato = Candidato.objects.get(pk=user.usuario)
    except:
        candidato = None
    context = { 'candidato': candidato }
    return render(request,"TrabalhoWeb/verCandidato.html", context)

def verEmpresa(request):
    user = request.user
    try:
        empresa = Empresa.objects.get(pk=user.usuario)
    except:
        empresa = None
    context = { 'empresa': empresa }
    return render(request,"TrabalhoWeb/verEmpresa.html", context)

def registro(request): 
    if request.method == 'POST': 
        formulario = UserCreationForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('home')
    else: 
        formulario = UserCreationForm()
    context = {'form': formulario} 
    return render(request, 'TrabalhoWeb/registro/registro.html', context)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.tipo == "EMPRESA":
            try:
                empresa = Empresa.objects.get(pk=user.usuario)
            except:
                empresa = None
            context = { 'Empresa': empresa }
            return render(request,"TrabalhoWeb/registro/homeEmpresa.html", context)
        try:
            candidato = Candidato.objects.get(pk=user.usuario)
        except:
            candidato = None
        context = { 'candidato': candidato }
        return render(request,"TrabalhoWeb/registro/homeCandidato.html", context)

class CandidatoView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': CandidatoModel2Form, }
        return render(request,"TrabalhoWeb/criaCandidato.html", context)

    def post(self, request, *args, **kwargs):
        formulario = CandidatoModel2Form(request.POST)
        if formulario.is_valid():
            candidato = formulario.save()
            candidato.usuario = request.POST["usuario"]
            candidato.save()
            return HttpResponseRedirect(reverse_lazy("sec-login"))
        else:
            context = {'candidato': formulario, }
            return render(request, 'TrabalhoWeb/atualizaCandidato.html', context)

class CandidatoListView(View):
 def get(self, request, *args, **kwargs):
    candidato = Candidato.objects.all()
    context = { 'candidato': candidato, }
    return render(request,'TrabalhoWeb/listaCandidato.html', context)

class CandidatoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        candidato = Candidato.objects.get(pk=pk)
        context = {'candidato': candidato, }
        return render(request, 'TrabalhoWeb/apagaCandidato.html', context)

    def post(self, request, pk, *args, **kwargs):
        candidato = Candidato.objects.get(pk=pk)
        candidato.delete()
        print("Removendo o candidato", pk)
        return HttpResponseRedirect(reverse_lazy("lista-candidato"))

class CandidatoUpdateView(View):
    def get(self, request, *args, **kwargs):   
        user = request.user
        candidato = Candidato.objects.get(pk=user.usuario)
        formulario = CandidatoModel2Form(instance=candidato)
        context = {'candidato': formulario, }
        return render(request, 'TrabalhoWeb/atualizaCandidato.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        candidato = get_object_or_404(Candidato, pk=user.usuario)
        formulario = CandidatoModel2Form(request.POST, instance=candidato)
        if formulario.is_valid():
            candidato = formulario.save()
            candidato.save()
            return HttpResponseRedirect(reverse_lazy("ver-candidato"))
        else:
            context = {'candidato': formulario, }
            return render(request, 'TrabalhoWeb/atualizaCandidato.html', context)

class EmpresaListView(View):
 def get(self, request, *args, **kwargs):
    empresa = Empresa.objects.all()
    context = { 'empresa': empresa, }
    return render(request,'TrabalhoWeb/listaEmpresa.html', context)

class EmpresaView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': EmpresaModel2Form, }
        return render(request,"TrabalhoWeb/criaEmpresa.html", context)

    def post(self, request, *args, **kwargs):
        formulario = EmpresaModel2Form(request.POST)
        if formulario.is_valid():
            empresa = formulario.save()
            empresa.usuario = request.POST["usuario"]
            empresa.save()
            return HttpResponseRedirect(reverse_lazy("sec-login"))
        else:
            context = {'empresa': formulario, }
            return render(request, 'TrabalhoWeb/atualizaEmpresa.html', context)