from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import UplaoadFileForm
from .excel_up.excel_load import excelLoad
from .models import WorkDate,WorkTime,WorkUser
from datetime import date
from django.utils import timezone
def index(request):
    today=date.today()
    print(today)
    dates=WorkDate.objects.filter(startWorkDate=today)
    context=[]
    for workDate in dates:
        workTime=workDate.time
       
        nowTime= timezone.localtime(timezone.now()).time()
        print(workDate.startWorkDate,workTime.start_time,workTime.end_time,nowTime)
        print(workTime.start_time <= nowTime <=workTime.end_time)
        userNumber={}
        if workTime.start_time <= nowTime <= workTime.end_time:
            
            users=workDate.user.all()
            for employees in users:
                userNumber[employees.userName]=employees.telNumber
                print(employees.userName,employees.telNumber)
        context.append(userNumber)
    print(context)
    return render(request,"home/index.html",{'content': context})

def excelUpload(request):
    if request.method == "POST":
        form = UplaoadFileForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                print("tamam")
                excelLoad(request.FILES["file"])
            except Exception as err:
                print(err)
 
            return redirect("/admin/")
    else:
        form = UplaoadFileForm()
        return render(request, "FileUpload/excel_upload.html", {"form": form})
# Create your views here.
