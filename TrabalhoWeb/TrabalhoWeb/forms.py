from django import forms
from TrabalhoWeb.models import Candidato, Empresa

class CandidatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'], label='Data do nascimento')
    
    class Meta:
        model = Candidato
        fields = '__all__'

class EmpresaModel2Form(forms.ModelForm):   
    class Meta:
        model = Empresa
        fields = '__all__'
