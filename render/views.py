from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

lapTime = 0
previouslyUp = False

def index(request):
    currentTime = datetime.time.minute
    print(currentTime)
    return render(request, 'render/index.html', {})
    # return HttpResponse(status=500)
