# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

def index(request):
	return render(request, 'polls/home.html')

def contact(request):
	return render(request, 'polls/basic.html', {'content':['If you would like to contact me' , 'smurf123444@gmail.com']})
