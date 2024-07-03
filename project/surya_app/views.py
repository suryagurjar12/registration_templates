from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration



# Create your views here.
def register(request):
    return render(request,'registration.html')


def registrationdata(request):
    
    print (request.method)
    print (request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    print(name,email,contact)
    Registration.objects.create(Name=name,Email=email,Contact=contact)
    print("Data Save Successfully")
    
    
