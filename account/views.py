from django.db import transaction
from django.shortcuts import render,HttpResponse,redirect
from account.models import User
from employee.models import Employee
# Create your views here.


def login(request):
    name = request.COOKIES.get("name")
    pwd = request.COOKIES.get("password")
    result = User.objects.filter(name=name,password=pwd)
    if result:
        request.session["login"] = "ok"
        return redirect("account:home")
    return render(request, "account/login.html")


def loginlogic(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    rem = request.POST.get("rember")
    result = User.objects.filter(name=name,password=pwd)
    if result:
        request.session["login"] = "ok"
        response = redirect('account:home')
        if rem:
            response.set_cookie("name",name,max_age=7*24*3600)
            response.set_cookie("password",pwd,max_age=7*24*3600)
        return response
    return HttpResponse("登陆失败")


def regist(request):
    return render(request, "account/regist.html")


def registlogic(request):
    try:
        with transaction.atomic():
            uname = request.POST.get("uname")
            name = request.POST.get("name")
            pwd = request.POST.get("pwd")
            sex = request.POST.get('sex')
            auto = request.POST.get('number')
            u = User.objects.filter(name=uname)
            if u:
                return HttpResponse("用户名已存在")
            User.objects.create(name=name, uname=uname, password=pwd, gender=sex, auto_code=auto, )
            return redirect("account:login")
    except Exception as a:
        print(a)
        return HttpResponse("注册失败")



def home(request):
    re = request.session.get("login")
    save = Employee.objects.all()
    if re:
        return render(request, "employee/emplist.html",{"save" : save})
        # return HttpResponse('22222222222222222')
    return redirect("account:login")