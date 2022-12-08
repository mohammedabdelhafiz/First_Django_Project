from django.shortcuts import render , redirect
from django.http import JsonResponse

def index(request):
    return redirect("/blogs")

def createuser(request):
    return render(request,'create.html')

def showw(request,number):
    context = {
        'number' : number
    }
    return render (request, 'num.html' , context)

def show(request,number):
    context = {
        'number' : number
    }
    return render (request, 'edit.html' , context)


    
    
