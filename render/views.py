from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    lapTime = 0
    previouslyUp = False
    while True:
        currentTime = datetime.time.minute
        if (currentTime >= lapTime+2):
            if (previouslyUp):
                previouslyUp = False
                lapTime = datetime.time.minute
                return HttpResponse(status=500)
            elif (not previouslyUp):
                previouslyUp = True
                lapTime = datetime.time.minute
                return render(request, 'render/index.html', {})