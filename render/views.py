from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
lapTime = 0

def index(request):
    lapTime = datetime.time.minute
    previouslyUp = True
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