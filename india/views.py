from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def jadeja(request):
    return HttpResponse('<center><h1>JADEJA</h1></center>')

