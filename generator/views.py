from django.shortcuts import render

from django.http import HttpResponse

import random 



# Create your views here.

def about(req):
    return render(req , 'generator/about.html')

def home(req):
    return render(req , 'generator/home.html' )

def password(req):
    
    characters = list('abcdefghijklmnoqprstuvwxyz')

    if req.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if req.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-+='))
        
    if req.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length =req.GET.get('length' , 12)
    thepassword = ''

    for x in range(int(length)):
        thepassword += random.choice(characters)

    return render(req , 'generator/password.html' , {'password':thepassword})
