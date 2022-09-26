from django.shortcuts import render
from .models import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail


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
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['badugudinesh94@gmail.com']) 
        return HttpResponse(sucess)
    
