from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
from .models import Logs
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
    request.session.flush()
    request.session['status'] = 'guest'
    return redirect('index')

def log(request):
    #current_date = datetime.datetime.now()
    if (request.session['status'] == 'guest'):
        return redirect('index')

    logs = Logs.objects.all()
    template = loader.get_template('log.html')

    data = ''
    for i in range(0, len(logs)):
        data += "<tr><td>"+(logs[i].time.strftime("%Y-%m-%d %H:%M:%S"))+"</td><td>"+logs[i].user_id+"</td></tr>"

    context = {
        'results': data,
        #'tes': logs[0].time,
    }

    return HttpResponse(template.render(context, request))

def setting(request):
    if request.method == 'GET':
        if (request.session['status'] == 'guest'):
            return redirect('index')
        template = loader.get_template('setting.html')
        context = {
            #'current_date': current_date,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('setting')

def lock(request):
    #current_date = datetime.datetime.now()
    if (request.session['status'] == 'guest'):
        return redirect('index')

    template = loader.get_template('lock.html')

    data = ''
    for i in range(0, len(logs)):
        data += "<tr><td>"+(logs[i].time.strftime("%Y-%m-%d %H:%M:%S"))+"</td><td>"+logs[i].user_id+"</td></tr>"

    context = {
        'results': data,
        #'tes': logs[0].time,
    }

    return HttpResponse(template.render(context, request))