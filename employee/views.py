from django.shortcuts import render,HttpResponse

# Create your views here.
from employee.models import Employee


def employee(request):
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    age = request.POST.get('age')
    operation = request.POST.get('operation')
    Employee.objects.create(name=name,salary=salary,age=age,operation=operation)
    return HttpResponse("添加成功")

