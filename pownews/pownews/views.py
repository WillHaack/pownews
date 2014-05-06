from django.shortcuts import render_to_response
from django.http import HttpResponse
from pownews.models import *

def index(request):
    links = LinkEntry.objects.order_by('hashed')[0:10]
    return render_to_response("index.html", links)
