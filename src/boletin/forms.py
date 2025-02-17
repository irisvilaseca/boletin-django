from django import forms
from .models import Registered

# This is a form based on the Registered model, including only the email field
class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registered
        fields = ["email"]

# This is a manual form
class RegForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
