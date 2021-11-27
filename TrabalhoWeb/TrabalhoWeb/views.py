from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'TrabalhoWeb/hello.html')

def SegundaPagina(request):
    return render(request, 'TrabalhoWeb/segunda.html')