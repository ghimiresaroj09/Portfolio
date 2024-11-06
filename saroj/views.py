from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    profile=Profile.objects.all()[0:1]
    project=Project.objects.all()   
    contact=Contact.objects.all()
    service=Service.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        cnt=Contact.objects.create(name=name,email=email,message=message)
        cnt.save()
        return redirect('home')
    
    return render(request, 'index.html',{'profile':profile,'project':project,'contact':contact,'service':service})
