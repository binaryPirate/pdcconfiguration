"""pdc_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from . import views

urlpatterns = [
    
    url(r'^$',views.index, name='pdc_configuration' ),
    url(r'^form/',views.simple_upload, name='load_file_form'),
    url(r'^server_cred/',views.envmt, name="server_cred"),
    url(r'^validate/',views.envmt, name="validate"),
    url(r'^show_configuration',views.show_configuration, name='show_configuration'),
    url(r'^(?P<config_id>[0-9]+)/$', views.call_jarvis, name='call_jarvis'),
    #url(r'^')
    
]
