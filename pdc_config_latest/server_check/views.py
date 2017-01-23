from django.shortcuts import render
from django.http import HttpResponse
from .models import servers
import os
# Create your views here.
def index(request):


    #pscpcmd="C:\\\"Program Files\"\\putty\\plink.exe -ssh -pw" + " " + password + " " +  username + "@" + hostname + " ps -ef | grep cm$"
   # pscpcmd="C:\\\"Program Files\"\\putty\\plink.exe -ssh -pw" + " " + "Gh4df!18st#"  + " " +  "brm" + "@" + "tr005stbrm.ddc.teliasonera.net" +" " + "ps -ef " +  " >>" +"C:\Users\chankaya.singh\Desktop\python_tool\django\pdc_config\server_check\Results\\test.txt"

    #print(pscpcmd)
    prwrdir = os.path.dirname(__file__)

    try :
        os.remove(prwrdir +"\\Results\\test.txt")
    except:
        print("no file present")

    srv=servers.objects.all()
    for s in srv:
        #open(prwdir + "\\temp_file\\ps_ef.txt","w").close()
    #    file=open("C:\Users\chankaya.singh\Desktop\python_tool\django\pdc_config\server_check\Results\\test.txt","a")
        srvname=s.hostname
        usrname=s.username
        pswd=s.password
        pscpcmd="C:\\\"Program Files\"\\putty\\plink.exe -ssh -pw" + " " + pswd  + " " +  usrname + "@" + srvname +" " + "ps -ef " +  " >>" + "C:\Users\chankaya.singh\Desktop\python_tool\\backup_pdc\latest\pdc_config_latest\server_check\Results\\test.txt"
        #pscpcmd="C:\\\"Program Files\"\\putty\\plink.exe -ssh -pw" + " " + pswd  + " " +  usrname + "@" + srvname +" " + "ps -ef " +  ">>" + prwrdir + "\\temp_file\\ps_ef.txt"
        print(pscpcmd)
        status=os.system(pscpcmd)

        if(status == 0 ):
            get_status("C:\\Users\\chankaya.singh\\Desktop\\python_tool\\backup_pdc\\latest\\pdc_config_latest\\server_check\\Results\\test.txt", s)
        #    get_status(prwrdir + "\\temp_file\\ps_ef.txt" , s)
        else:
            print("connection error for" + s.hostname )
            s.status="err"

        #pscpcmd="C:\\\"Program Files\"\\putty\\plink.exe -ssh -pw" + " " + pswd  + " " +  usrname + "@" + srvname +" " + "-m" + " " + "C:\Users\chankaya.singh\Desktop\python_tool\\backup_pdc\latest\pdc_config_latest\server_check\commands\cmd.txt" # +  " >>" + "C:\Users\chankaya.singh\Desktop\python_tool\django\pdc_config\server_check\Results\\test.txt"
        #status=os.system(pscpcmd)
    #    if(status != 0):
    #        print "connection error"




        print("status of the command is " + str(status) )
    #file=open('output.txt','w')
    #buff=os.system(pscpcmd)
   # print("here is what we were not expecting buffer $$$$$$$" + " " + str(buff))
    #file.write(os.system(pscpcmd))
    context={
        'server':srv
        }
    return render(request,'server_check/index.html',context)


def get_status(file, models ):
    print "inside get_status" + " " + models.hostname
    with open(file) as fil:
        for f in fil:
            if "dm_oracle" in f:
                models.dm_oracle="UP"

            if "Deai_js" in f:
                models.java_Deai_js="UP"

            if "Dformatter" in f:
                models.java_formater="UP"

            if "cm" in f:
                models.cm="UP"

            if "wirelessRealtime" in f:
                models.syc_pdc="UP"

            if "bre" in f:
                models.bre="UP"

            if "rre" in f:
                models.rre="UP"

            models.save()
