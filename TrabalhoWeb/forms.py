from django import forms
from TrabalhoWeb.models import Candidato, Empresa, Usuario

class CandidatoModel2Form(forms.ModelForm):
    
    class Meta:
        model = Candidato
        fields = ('nome', 'email', 'telefone', 'cidade', 'estado', 'pais', 'descricao', 'experiencia', 'formacao', 'cargo', 'estadoCivil', 'sexo', 'endereco')

class UsuarioModel2Form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpresaModel2Form(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome', 'email', 'telefone', 'endereco', 'descricao')

