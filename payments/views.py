import email
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.shortcuts import render, redirect
# from django.contrib.auth.models import User , auth
# Create your views here.
@csrf_exempt
def handlerequest(request):
    return HttpResponse('Payment Done')


    