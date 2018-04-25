from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
import hashlib
import datetime
from django.template import loader
from django.shortcuts import redirect
from django.db import connections

def index(request):
    request.session['status'] = 'guest'
    return render(request, 'login.html', {})

def login(request):
    if request.method == 'POST':
        #get form data
        user = Users()
        user.user_id = request.POST['id']

        pwd = (request.POST['pwd']).encode()
        user.password = hashlib.sha256(pwd).hexdigest()

        cek = len(Users.objects.filter(user_id = user.user_id, password = user.password))

        if ( cek == 1):
            template = loader.get_template('tes.html')
            context = {
                'user_id' : user.user_id,
                'password' : user.password,
                #'tes' : tes
            }

            hasil = Users.objects.all()

            #return HttpResponse(template.render(context, request))
            request.session['status'] = 'user'
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id
            return redirect('home')
        else:
            return redirect('index')
    else:
        return redirect('index')

def home(request):
    #current_date = datetime.datetime.now()
    if (request.session['status'] == 'guest'):
        return redirect('index')
    template = loader.get_template('home.html')
    context = {
        #'current_date': current_date,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    #current_date = datetime.datetime.now()
    template = loader.get_template('home.html')
    context = {
        #'current_date': current_date,
    }
    #return HttpResponse(template.render(context, request))
    request.session.flush()
    request.session['status'] = 'guest'
    return redirect('index')

def tes(request):
    current_date = datetime.datetime.now()
    template = loader.get_template('tes.html')
    context = {
        'current_date': current_date,
    }
    return HttpResponse(template.render(context, request))