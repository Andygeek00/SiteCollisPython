from django.shortcuts import render
from django.http import HttpResponse
from .forms  import RegisterParcelForm
from .models import Parcel



# Create your views here.

def home_page(request):
    nb_colis = len(Parcel.objects.all())
    context = {
        "nb_colis": nb_colis,
        "nom_entrepot": "AWANAX.corp"
    }
    return render(request, 'index.html',context=context)


def tracking_page(request):
    parcel = None
    error = None
    if request.method == 'POST':
        # Recuperation de la valeur du champ tracking number
        tracking_number = request.POST.get('tracking_number')

        try:
            parcel = Parcel.objects.get(tracking_number=tracking_number)
        except Parcel.DoesNotExist:
            error = "No package exists with this tracking"

    return render(request,"tracking.html",{"parcel": parcel, "error": error})
    


def parcels_page(request):
    return render(request, "parcels.html",context={"colis": Parcel.objects.all() })


def add_parcels(request):

    if request.method == "POST":
        # Recuperation des données saisies dans le formulaire
        form = RegisterParcelForm(request.POST)
        if form.is_valid():
            form.save() # insertion dans la base de données
            return HttpResponse('Package recorded')
    else:
        form = RegisterParcelForm()
        return render(request, "add_parcels.html", context={"form": form})


