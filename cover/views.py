
from tokenize import Double
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ContactUs, MedicalEm, StartUp, Payments
from django.contrib.auth.models import User
from django.contrib import messages

from PayTm import Checksum
# MERCHANT_KEY = 
# from django.contrib.auth.models import User , auth
# Create your views here.



def cover(request):
    return render(request, 'cover.html')

def home(request):
    return render(request, 'home.html')

def contactUs(request):
    if request.method =='POST':
       pass
       name = request.POST['name']
       email = request.POST['email'] 
       phone = request.POST['phone']
       msg = request.POST['msg']

       query = ContactUs(name=name, email=email, phone=phone, msg=msg)
       query.save();
       messages.info(request,'Message sent!')
       return redirect('/contactUs/')
    else:
        return render(request, 'contactUs.html')

def startup(request):
    if request.method =='POST':
        ammount = request.POST['ammount']
        val = Payments(ammount=ammount)

        val.save();
           
        param_dict={

                'MID': '',
                'ORDER_ID': 'id',
                'TXN_AMOUNT': '750.00',
                'CUST_ID': 'id',
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/payments/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, merchant_key="")
        return  render(request, 'paytm.html', {'param_dict': param_dict})
       
    else:
        startups = StartUp.objects.all()
        # startups.funded = (startups.fund_raised/startups.fund_req)*100
        return render(request, 'startup.html', {'startups': startups})



def medicalEm(request):
    patients = MedicalEm.objects.all()
    return render(request, 'medicalEm.html', {'patients': patients})


# def payments(request):
#     if request.method=='POST':
#         pass
#     else:
#         return render(request, 'payments.html')

