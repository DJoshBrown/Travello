from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
In this file we create our view for the app.
we define our view, as a functions with a request parameter, and will respond with an httpresponse

The current 'home()' will only return a simple "Hello World" message
"""

def home(request):
    return render(request, 'home.html', {'name' : 'Josh'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    
    res =  val1 + val2

    return render(request, 'result.html', {'result': res})