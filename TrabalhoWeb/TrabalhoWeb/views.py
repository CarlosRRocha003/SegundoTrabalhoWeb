from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls.base import reverse_lazy
from TrabalhoWeb.models import Candidato, Usuario, Empresa
from TrabalhoWeb.forms import CandidatoModel2Form, UsuarioModel2Form, EmpresaModel2Form
from django.contrib.auth import authenticate, login
from TrabalhoWeb.admin import UserCreationForm
from django.contrib.auth.views import LoginView
from django.template import RequestContext
import datetime
# Create your views here.
def home(request):
    try:
        if request.user.tipo == "EMPRESA":
            return redirect('ver-empresa')
        else:
            return redirect('ver-candidato')
    except:
        return redirect('sec-login')

def loginHome(request):
    return render(request, 'TrabalhoWeb/login.html')

def profile(request):
    return redirect('home')

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
class CandidatoView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': CandidatoModel2Form, }
        return render(request,"TrabalhoWeb/criaCandidato.html", context)

    def post(self, request, *args, **kwargs):
        formulario = CandidatoModel2Form(request.POST)
        print(request.POST)
        if formulario.is_valid():
            print("---------------------------------------------------------------------------OIIIIIII")
            candidato = formulario.save()
            print("---------------------------------------------------------------------------OIIIIIII")
            candidato.usuario = request.POST["usuario"]
            print("---------------------------------------------------------------------------OIIIIIII")
            candidato.dtNasc = request.POST["dtNasc"]
            print("---------------------------------------------------------------------------OIIIIIII")
            print(candidato.dtNasc)
            candidato.save()
            return HttpResponseRedirect(reverse_lazy("ver-candidato"))
        else:
            context = {'candidato': formulario, }
            return render(request, 'TrabalhoWeb/atualizaCandidato.html', context)

class CandidatoListView(View):
 def get(self, request, *args, **kwargs):
    candidato = Candidato.objects.all()
    context = { 'candidato': candidato, }
    return render(request,'TrabalhoWeb/listaCandidato.html', context)

class CandidatoDeleteView(View):
    def get(self, request, *args, **kwargs):  
        user = request.user
        candidato = Candidato.objects.get(pk=user.usuario)
        context = {'candidato': candidato, }
        return render(request, 'TrabalhoWeb/apagaCandidato.html', context)

    def post(self, request, *args, **kwargs):  
        user = request.user
        candidato = Candidato.objects.get(pk=user.usuario)
        candidato.delete()
        return HttpResponseRedirect(reverse_lazy("ver-candidato"))

class EmpresaDeleteView(View):
    def get(self, request, *args, **kwargs):  
        user = request.user
        empresa = Empresa.objects.get(pk=user.usuario)
        context = {'empresa': empresa, }
        return render(request, 'TrabalhoWeb/apagaEmpresa.html', context)

    def post(self, request, *args, **kwargs):  
        user = request.user
        empresa = Empresa.objects.get(pk=user.usuario)
        empresa.delete()
        return HttpResponseRedirect(reverse_lazy("ver-empresa"))

class EmpresaUpdateView(View):
    def get(self, request, *args, **kwargs):   
        user = request.user
        empresa = Empresa.objects.get(pk=user.usuario)
        formulario = EmpresaModel2Form(instance=empresa)
        context = {'empresa': formulario, }
        return render(request, 'TrabalhoWeb/atualizaEmpresa.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        empresa = get_object_or_404(Empresa, pk=user.usuario)
        formulario = EmpresaModel2Form(request.POST, instance=empresa)
        if formulario.is_valid():
            empresa = formulario.save()
            empresa.save()
            return HttpResponseRedirect(reverse_lazy("ver-empresa"))
        else:
            context = {'empresa': formulario, }
            return render(request, 'TrabalhoWeb/atualizaEmpresa.html', context)

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
            return HttpResponseRedirect(reverse_lazy("ver-empresa"))
        else:
            context = {'empresa': formulario, }
            return render(request, 'TrabalhoWeb/atualizaEmpresa.html', context)

def handler404(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

def verificaDtNasc(request):
    dtNasc = request.GET.get("dtNasc", None)
    date2 = dtNasc.split("-")
    year = int(date2[0])
    month = int(date2[1])
    day = int(date2[2])
    d = datetime.date(year,month,day)
    today = datetime.date.today()
    if today > d:
        resposta = {'valido': True}
    else:
        resposta = {'valido': False}
    return JsonResponse(resposta)