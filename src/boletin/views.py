from django.shortcuts import render
from .forms import RegForm
from .models import Registered
# Create your views here.
def index(request):
    form=RegForm(request.POST or None)
    if form.is_valid():
        form_data=form.cleaned_data
        abc=form_data.get("email")
        abc2=form.data.get("name")
        obj=Registered.objects.create(email=abc,name=abc2)
    context={
        "form":form,
    }
    return render(request,"index.html",context)