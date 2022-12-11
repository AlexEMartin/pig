from django import forms
from .models import Almohadon, Customer

class AlmohadonForm(forms.ModelForm):
    class Meta:
        model = Almohadon
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
