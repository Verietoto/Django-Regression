from django.shortcuts import render, redirect
from django.http import HttpResponse
import django
from firstapp.forms import Regresi_form
from firstapp.models import regression_db
from firstapp.graphy import empty_graph
# Create your views here.

def index(request):
    empty_graph()
    if request.method == "POST":
        form = Regresi_form(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            regresion_database = regression_db()

            #Add new
            regression_db.objects.create(x_val=x, y_val=y)
            form = Regresi_form()
            return redirect('/')
    else:    
        form = Regresi_form()
        return render(request, 'index.html', {'form': form, 'regression': regression_db.objects.all()})

def clear_database(request):
    regression_db.objects.all().delete()
    return redirect('/')