from django.http import Http404
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from datetime import datetime


from .models import Escola, Estudi, Oferta



def index(request):

    #llistat_estudis = Estudi.objects.order_by("nom")
    #carrerga el template
    #template = loader.get_template("index.html")
    #context = {
    #"llistat_estudis":llistat_estudis,
    #} 

    any_actual = datetime.now().year

    llistat_escoles = Escola.objects.order_by("nom")
    template = loader.get_template("index.html")
    context = {
    "llistat_escoles":llistat_escoles,
    "any_actual":any_actual
    } 

    return HttpResponse(template.render(context,request))



def detall(request,escola_id):
    
    try:
        escola = Escola.objects.get(pk=escola_id)

    except escola.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, "detall.html", {"escola" : escola})


def estudis_per_any(request, escola_id, any_oferta):

    escola = Escola.objects.get(pk=escola_id)
    ofertes = Oferta.objects.filter(escola=escola, any_oferta=any_oferta)
    estudi = [oferta.estudi for oferta in ofertes]

    context = {
        'escola': escola,
        'any_oferta': any_oferta,
        'estudis': estudi
    }
    return render(request, "estudis_per_any.html", context)

