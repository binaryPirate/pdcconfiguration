from django import forms

class UploadFileForm(forms.Form):
    file=forms.FileField()
    


class Selectenv(forms.Form):
    host_name=forms.CharField(max_length=100)
    usrname=forms.CharField(max_length=30)
    passwd=forms.CharField(max_length=20)
    
    source=forms.CharField(max_length=1000)
    destination=forms.CharField(max_length=1000)
    
