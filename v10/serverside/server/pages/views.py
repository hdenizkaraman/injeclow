from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/acc/getin/")
def index(request):
    return render(request, "index.html")
    
@login_required(login_url="/acc/getin/")
def actions(request):
    
    return render(request, "hareketler.html")