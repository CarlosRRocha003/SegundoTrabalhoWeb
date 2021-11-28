from django import forms
from TrabalhoWeb.models import Candidato, Empresa, Usuario

class CandidatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'], label='Data de Nascimento', help_text='Nascimento no formado DD/MM/AAAA')
    
    class Meta:
        model = Candidato
        fields = ('nome', 'email', 'telefone', 'dtNasc', 'cidade', 'estado', 'pais', 'descricao', 'experiencia', 'formacao', 'cargo', 'estadoCivil', 'sexo', 'endereco')

class UsuarioModel2Form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpresaModel2Form(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome', 'email', 'telefone', 'endereco', 'descricao')

