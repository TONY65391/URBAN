from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import amount
from . forms import FORM

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request))

def images(request):
    template = loader.get_template('images.html')
    return HttpResponse(template.render(request = request))

def next_page(request):
    template = loader.get_template('next_page.html')
    return HttpResponse(template.render(request = request))

def coffee_table(request):
    form = FORM
    context = {'form':form}
    template = loader.get_template('coffee_table.html')
    return HttpResponse(template.render(request = request, context = context))

def aurora_shelf(request):
    form = FORM
    context = {'form':form}
    template = loader.get_template('5-row-shelf.html')
    return HttpResponse(template.render(request = request, context = context))

def pendant_lamp(request):
    form = FORM
    context = {'form':form}
    template = loader.get_template('aurora-pendaant-lamp.html')
    return HttpResponse(template.render(request = request, context = context))