from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import cuentaFORM

def index(request):
    if request.method == 'POST':
        form = cuentaFORM(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = cuentaFORM()
    return render(request, 'index.html',{'form':form})
