# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime, timedelta
from django.utils import timezone
from bonito.models import temperatura


#------------------------------- Principal ------------------------------------------------------

def home(request):
    las_temperaturas = temperatura.objects.order_by('-fecha')
    context = {'las_temperaturas': las_temperaturas }
    return render(request, 'bonito/home.html', context)
