from django import forms
from . models import amount

class FORM(forms.ModelForm):
    class Meta:
        model = amount
        fields = '__all__'