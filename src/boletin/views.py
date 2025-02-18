from django.shortcuts import render
from .forms import RegModelForm
from .models import Registered
# Create your views here.
def index(request):
    title="Hello"
    if request.user.is_authenticated:
        title=f"Welcome {request.user}"
    form=RegModelForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print(instance)
        instance.save()
        print(instance)
        print(instance.timestamp)
        #form_data=form.cleaned_data
        #abc=form_data.get("email")
        #abc2=form.data.get("name")
        #obj=Registered.objects.create(email=abc,name=abc2)
    context={
        "title":title,
        "form":form,
    }
    return render(request,"index.html",context)