from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def khan(request):
    return render(request,'khan.html')

def azam(request):
    return HttpResponse('<center><h1>azam creakater</h1></center>')