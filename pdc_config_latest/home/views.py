from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request

from django.template.context import RequestContext
# Create your views here.
def index(request):
   return render(request,'home/index.html')



def pdc_configuration(request):
    return render(request,'home/pdc_configuration.html',context_instance=RequestContext(request))


def about(request):
    return HttpResponse("hiii about page")


def contact(request):
    return HttpResponse("hii contact page")

def tutorials(request):
    return HttpResponse("here we will get turorial")
