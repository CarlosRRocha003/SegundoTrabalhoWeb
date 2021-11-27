from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from TrabalhoWeb.models import Candidato, Empresa
from TrabalhoWeb.forms import CandidatoModel2Form, EmpresaModel2Form
# Create your views here.
def home(request):
    return render(request, 'TrabalhoWeb/home.html')

def SegundaPagina(request):
    return render(request, 'TrabalhoWeb/criaCandidato.html')

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
