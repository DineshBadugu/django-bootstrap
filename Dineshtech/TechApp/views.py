from django.shortcuts import render
from .models import ContactForm
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,"uifiles/index.html")

def ConctactData(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        
        oContactinfo = ContactForm(Name=name,Email=email,Subject=subject,Message=message)
        oContactinfo.save()
        sucess =f'hi {name} sucessfully Sending email'
        return HttpResponse(sucess)
    #return render(request,'uifiles/base.html')