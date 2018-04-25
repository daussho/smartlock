from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
import hashlib
import datetime
from django.template import loader
from django.shortcuts import redirect
from django.db import connections

def index(request):
    return render(request, 'login.html', {})

def login(request):
    if request.method == 'POST':
        #get form data
        user = Users()
        user.user_id = request.POST['id']

        pwd = (request.POST['pwd']).encode()
        user.password = hashlib.sha256(pwd).hexdigest()

        cek = len(Users.objects.filter(user_id = user.user_id))

        if ( cek == 1):
            template = loader.get_template('tes.html')
            context = {
                'user_id' : user.user_id,
                'password' : user.password,
                'tes' : tes
            }

            hasil = Users.objects.all()

            return HttpResponse(template.render(context, request))
        else:
            return redirect('home')
    else:
        return redirect('index')

def home(request):
    #current_date = datetime.datetime.now()
    template = loader.get_template('home.html')
    context = {
        #'current_date': current_date,
    }
    return HttpResponse(template.render(context, request))

def tes(request):
    current_date = datetime.datetime.now()
    template = loader.get_template('tes.html')
    context = {
        'current_date': current_date,
    }
    return HttpResponse(template.render(context, request))