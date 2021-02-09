from django.shortcuts import render
from django.http import HttpResponse

import sys

# Create your views here.


def index(request):
    if (sys.stdin == "up"):
        return render(request, 'render/index.html', {})
    elif (sys.stdin == "down"):
        return HttpResponse(status=500)
    else:
        return HttpResponse(status=500)

