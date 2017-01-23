from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from .models import post, comments
def index(request):
     p=post.objects.all()
     comment=comments.objects.all()
     template = loader.get_template('knowledgexchange/index.html')
     context={
     'post':p,

     }
     return HttpResponse(template.render(context,request))
