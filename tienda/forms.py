from django import forms
from .models import Almohadon

class AlmohadonForm(forms.ModelForm):
    class Meta:
        model = Almohadon
        fields = '__all__'