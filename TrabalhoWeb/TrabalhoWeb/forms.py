from django import forms
from TrabalhoWeb.models import Candidato

class CandidatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'], label='Data do nascimento')
    
    class Meta:
        model = Candidato
        fields = '__all__'
