from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Hareket

# Create your views here.
@login_required(login_url="/acc/getin/")
def index(request):
    return render(request, "index.html")
    
@login_required(login_url="/acc/getin/")
def actions(request):
    act = Hareket.objects.all()
    context = {
        "hareket": act,
    }
    return render(request, "hareketler.html", context)

@login_required(login_url="/acc/getin/")
def aktifet(request, slug):
    spesificact = Hareket.objects.get(slug=slug)
    spesificact.activity = 1
    spesificact.save()
    return redirect("hareketler")

@login_required(login_url="/acc/getin/")
def pasifet(request, slug):
    spesificact = Hareket.objects.get(slug=slug)
    spesificact.activity = 0
    spesificact.save()
    return redirect("hareketler")

def veriler(request):
    acts = Hareket.objects.all()
    context = {"hareket":acts,}
    return render(request, "veriler.html", context)