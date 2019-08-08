from django.http import HttpResponse
from django.shortcuts import render

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)  
    )