# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'polls/home.html')

def contact(request):
	return render(request, 'polls/basic.html')



