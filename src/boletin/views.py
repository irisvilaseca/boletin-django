from django.shortcuts import render
from .forms import RegForm
# Create your views here.
def index(request):
    form=RegForm()
    context={
        "form":form,
    }
    return render(request,"index.html",context)