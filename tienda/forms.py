from django import forms
from .models import Almohadon, Funda

class AlmohadonForm(forms.ModelForm):
    class Meta:
        model = Almohadon
        fields = '__all__'
        
        

class FundaForm(forms.ModelForm):
    
    class meta:
        model = Funda
        fields = '__all__'