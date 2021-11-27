from django import forms
from TrabalhoWeb.models import Candidato, Usuario

class CandidatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'], label='Data de Nascimento', help_text='Nascimento no formado DD/MM/AAAA')
    
    class Meta:
        model = Candidato
        fields = '__all__'

class UsuarioModel2Form(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = '__all__'
