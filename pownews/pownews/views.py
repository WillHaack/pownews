from django.shortcuts import render_to_response
from django.http import HttpResponse
from pownews.models import *
from django.template import RequestContext
from hashlib import sha256

def index(request):
    links = LinkEntry.objects.order_by('hashed')[0:10]
    formattedLinks = formatLinks(links)
    return render_to_response("index.html", {'links': formattedLinks},
      context_instance=RequestContext(request))

def formatLinks(queryLinks):
    formattedLinks = []
    for link in queryLinks:
      formattedLink = {}
      formattedLink['link'] = link.link
      formattedLink['nonce'] = link.nonce
      formattedLink['hash'] = link.hashed
      formattedLinks.append(formattedLink)
    return formattedLinks

def addLink(request):
  link = request.POST['link']
  nonce = request.POST['nonce']
  hashed = sha256(link + nonce).hexdigest()
  
