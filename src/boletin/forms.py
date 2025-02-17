from django import forms
from .models import Registered

# This is a form based on the Registered model, including the email and the name fields
class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registered
        fields = ["email","name"]
    #This function is a personalized validation method 
    def clean_email(self):
        email=self.cleaned_data.get("email")
        email_base, provider=email.split("@")
        domain,extension=provider.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Please use an email with EDU as extension")
        return email
    def clean_name(self):
        name=self.cleaned_data.get("name")
        return name

# This is a manual form
class RegForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
