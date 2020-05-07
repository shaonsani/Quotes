from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

def employee_list(req):
    context = {'employee_list':Employee.objects.all()}
    return render(req,'Quotes/employee_list.html',context)

def employee_form(req,id=0):
    para=False
    if req.method =='GET':
        if id==0:                   # This condition is for Insert, when insert id =0
            form =EmployeeForm()
        else:                        # This condition is for Update, when update btn click corresponding employee key is passed
            from_database = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=from_database)
            para =True
        dist = {'form':form,'para':para}
        return render(req,'Quotes/employee_form.html',context=dist)
    else:
        if id==0:
            form =EmployeeForm(req.POST)
        else:
            from_database= Employee.objects.get(pk=id)
            form = EmployeeForm(req.POST,instance=from_database)
        if form.is_valid():
            form.save()
        return redirect('/Quotes/list')

def employee_delete(req,id):
    from_database= Employee.objects.get(pk=id)
    from_database.delete()
    return redirect('/Quotes/list')
