from django.shortcuts import render,redirect
from .forms import QuotesForm
from .models import Quotes

def Quotes_list(req):
    context = {'quotes_list':Quotes.objects.all()}
    return render(req,'Quotes/quotes_list.html',context)

def Quotes_form(req,id=0):
    para=False
    if req.method =='GET':
        if id==0:                   # This condition is for Insert, when insert id =0
            form =QuotesForm()
        else:                        # This condition is for Update, when update btn click corresponding employee key is passed
            from_database = Quotes.objects.get(pk=id)
            form = QuotesForm(instance=from_database)
            para =True
        dist = {'form':form,'para':para}
        return render(req,'Quotes/quotes_form.html',context=dist)
    else:
        if id==0:
            form =QuotesForm(req.POST)
        else:
            from_database= Quotes.objects.get(pk=id)
            form = QuotesForm(req.POST,instance=from_database)
        if form.is_valid():
            form.save()
        return redirect('/list')

def Quotes_delete(req,id):
    from_database= Quotes.objects.get(pk=id)
    from_database.delete()
    return redirect('/list')
