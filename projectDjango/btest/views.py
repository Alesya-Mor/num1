from .models import *
from django.shortcuts import render
 
def index(request):
    bbs = Collection.objects.all()
    rbs = Exponat.objects.all()
    tbs = Zal.objects.all()
    
    return render(request, "btest/index.html", {'bbs': bbs, 'rbs1': rbs, 'tbs': tbs })

