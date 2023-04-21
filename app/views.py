from operator import itemgetter
from django.shortcuts import render
from django.db.models import Q
# Create your views here.

from app.models import *
from datetime import date
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def home(request):
    return render(request,'HOME.html')
def menu(request):
    return render(request,'MENU.html')

def about(request): 
    return render(request,'ABOUT.html')

def records(request):
    return render(request,'RECORDS.html')

def billing(request):
    orderform=Order_form()
    d={'orderform':orderform}
    if request.method=='POST':
        neworder=Order_form(request.POST)
        if neworder.is_valid():
            
            item=neworder.cleaned_data['item']
            menuobj=Menu.objects.get(item=item)
            price=menuobj.price
            qty=neworder.cleaned_data['qty']
            amount=price*qty
            neworder_obj=Order.objects.get_or_create(item=item,price=price,qty=qty,amount=amount)[0]
            neworder_obj.save()
            d={'neworder':neworder_obj}
        return render(request,'neworder.html',d)
    return render(request,'BILLING.html',d)




def detailed_daily_report(request):
    dateform=Date_form()
    d={'getdate':dateform}
    if request.method=='POST':
        newdate=Date_form(request.POST)
        if newdate.is_valid():
            day=newdate.cleaned_data['date']
            detaileddailyreport=Order.objects.filter(date=day)
            d={'report':detaileddailyreport}
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)

def daily_report(request):
    dateform=Date_form()
    d={'getdate':dateform}
    if request.method=='POST':
        newdate=Date_form(request.POST)
        if newdate.is_valid():
            day=newdate.cleaned_data['date']
            menuobj=Menu.objects.all()
            Report.objects.all().delete()
            for i in menuobj:
                 totalqty=0
                 detaileddailyreport=Order.objects.filter(Q(date=day)&Q(item=i))
                 for j in detaileddailyreport:
                    totalqty+=j.qty
                 reportobj=Report.objects.create(date=day,item=i,price=i.price,qty=totalqty,amount=i.price*totalqty)
            reports=Report.objects.all()
            d={'report':reports}
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)




def monthly_report(request):
    monthform=Month_form()
    d={'getdate':monthform}
    if request.method=='POST':
        newmonth=Month_form(request.POST)
        if newmonth.is_valid():
            month=newmonth.cleaned_data['month']
            menuobj=Menu.objects.all()
            Report.objects.all().delete()
            for i in menuobj:
                 totalqty=0
                 detaileddailyreport=Order.objects.filter(Q(date__month=month)&Q(item=i))
                 for j in detaileddailyreport:
                    totalqty+=j.qty
                 reportobj=Report.objects.create(date=month,item=i,price=i.price,qty=totalqty,amount=i.price*totalqty)
            reports=Report.objects.all()
            d={'report':reports}            
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)


def detailed_monthly_report(request):
    monthform=Month_form()
    d={'getdate':monthform}
    if request.method=='POST':
        newmonth=Month_form(request.POST)
        if newmonth.is_valid():
            month=newmonth.cleaned_data['month']
            detailedmonthlyreport=Order.objects.filter(date__month=month)
            d={'report':detailedmonthlyreport}
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)



def detailed_yearly_report(request):
    yearform=Year_form()
    d={'getdate':yearform}
    if request.method=='POST':
        newyear=Year_form(request.POST)
        if newyear.is_valid():
            year=newyear.cleaned_data['year']
            detailedyearreport=Order.objects.filter(date__year=year)
            d={'report':detailedyearreport}
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)

def yearly_report(request):
    yearform=Year_form()
    d={'getdate':yearform}
    if request.method=='POST':
        newmonth=Year_form(request.POST)
        if newmonth.is_valid():
            year=newmonth.cleaned_data['year']
            menuobj=Menu.objects.all()
            Report.objects.all().delete()
            for i in menuobj:
                 totalqty=0
                 detaileddailyreport=Order.objects.filter(Q(date__year=year)&Q(item=i))
                 for j in detaileddailyreport:
                    totalqty+=j.qty
                 reportobj=Report.objects.create(date=year,item=i,price=i.price,qty=totalqty,amount=i.price*totalqty)
            reports=Report.objects.all()
            d={'report':reports}            
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)