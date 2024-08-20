from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)

def pageDeRFID(request):
    return render(request, "RFID.html")

def pageDeBiométrique(request):
    return render(request, "Biometrique.html")

def accueil(request):
    return render(request, "accueil.html")

def hospitalisation(request):
    return render(request, "hospitalisation.html")

def attente(request):
    return render(request, "attente.html")

def consultation(request):
    return render(request, "consultation.html")

def consBio(request):
    return render(request, "consBio.html")

def accueilPat(request):
    return render(request, "accueilPat.html")

def Ordonnace(request):
    return render(request, "Ordonnace.html")

from django.shortcuts import render

def impression(request):
    if request.method == "POST":
        noms = request.POST.getlist('nom[]')
        posologies = request.POST.getlist('posologie[]')
        methodes = request.POST.getlist('methode[]')

        # Combinez les listes en une liste de tuples
        combined_data = zip(noms, posologies, methodes)

        return render(request, 'impressionOrd.html', {
            'combined_data': combined_data
        })
    return HttpResponse("Invalid request", status=400)
