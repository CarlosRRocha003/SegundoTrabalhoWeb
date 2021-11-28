from django import forms
from TrabalhoWeb.models import Candidato, Empresa, Usuario

class CandidatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'], label='Data de Nascimento', help_text='Nascimento no formado DD/MM/AAAA')
    
    class Meta:
        model = Candidato
        fields = '__all__'

class UsuarioModel2Form(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = '__all__'


class EmpresaModel2Form(forms.ModelForm):   
    class Meta:
        model = Empresa
        fields = '__all__'
