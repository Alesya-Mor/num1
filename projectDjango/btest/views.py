from .models import *
from django.shortcuts import render
 
def index(request):
    bbs = Bb.objects.all()
    rbs = Rubric.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs, 'rbs1': rbs})

