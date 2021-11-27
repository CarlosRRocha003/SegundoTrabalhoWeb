from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from TrabalhoWeb.models import Candidato
from TrabalhoWeb.forms import CandidatoModel2Form
# Create your views here.
def home(request):
    return render(request, 'TrabalhoWeb/hello.html')

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

class CandidatoListView(View):
 def get(self, request, *args, **kwargs):
    candidato = Candidato.objects.all()
    context = { 'candidato': candidato, }
    return render(request,'TrabalhoWeb/listaCandidato.html', context)
