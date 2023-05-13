from django.shortcuts import render

from . forms import FormLogin

# Create your views here.

def index(request) :

    form_login = FormLogin()

    context = {
        'login' : form_login
    }

    return render(request, 'login/index.html')