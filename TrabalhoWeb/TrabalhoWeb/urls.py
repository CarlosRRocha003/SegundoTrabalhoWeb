"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView
from TrabalhoWeb.forms import CandidatoModel2Form

import TrabalhoWeb.views
from TrabalhoWeb import views

urlpatterns = [
    path('', views.LoginView.as_view()),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/login/', LoginView.as_view(template_name='TrabalhoWeb/registro/login2.html'), name='sec-login'), 
    path('accounts/profile/', views.paginaSecreta, name='sec-paginaSecreta'), 
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('CriaCandidato', views.CandidatoView.as_view(), name='cria-candidato'),
    path('ListaCandidato', views.CandidatoListView.as_view(), name='lista-candidato'),
    path('CriaEmpresas', views.EmpresaView.as_view(), name='cria-empresa'),
    path('ListaEmpresas', views.EmpresaListView.as_view(), name='lista-empresa')
]
