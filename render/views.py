from django.shortcuts import render
from django.http import HttpResponse

import sys

# Create your views here.


def index(request):
    # return render(request, 'render/index.html', {})
    return HttpResponse(status=500)

