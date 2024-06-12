from django.shortcuts import render,redirect ,HttpResponse
from  todoapp.models import todomodl
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout

def home(request):
    alltodo = todomodl.objects.all()

    return render(request,"home.html",{'alltodoo':alltodo ,"checkout":"home"})


def showdata(request):
    if request.method == "POST":
        Tit = request.POST.get("title")
        des = request.POST.get("description")
        img = request.FILES.get("img")

        alldata = todomodl(title = Tit, description = des,imag = img)
        alldata.save()




    
    return redirect("home")



def remove(request, id):
    td = todomodl.objects.get(id=id)
    td.delete()
    return redirect("home")



def update(request, id):
    if request.method == "POST":
        altd = todomodl.objects.all()
        todo = todomodl.objects.get(id=id)
        



    return render(request,"home.html",{"todos":altd ,"todo":todo , "checkout":"update"})


def updatenaow(request,id):
    mytd = todomodl.objects.get(id=id)
    if request.method == "POST":
        nm = request.POST.get("title")
        ds = request.POST.get("description")
        mytd.title = nm
        mytd.description = ds

        mytd.save()





    return redirect("home")



def signup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        fname = request.POST.get("name")
        em =  request.POST.get("email")
        pas = request.POST.get("passw")

        xxx = User.objects.create_user(username=uname,email=em,first_name = fname,password= pas)
        xxx.save()


    return HttpResponse("success")


# login pending
def loginfunction(request):
    return HttpResponse("successlogin")