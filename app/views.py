from operator import itemgetter
from django.shortcuts import render
from django.db.models import Q
import datetime
# Create your views here.

from app.models import *
from datetime import date
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def home(request):
    return render(request,'HOME.html')
def menu(request):
    menuobj=Menu.objects.all()
    d={'menu':menuobj}
    return render(request,'MENU.html',d)

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
            d={'report':detaileddailyreport,'detailed_daily_report':'detailed_daily_report'}
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
            d={'report':reports,'daily_report':'daily_report'}
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)




def monthly_report(request):
    monthform=Month_form()
    d={'getdate':monthform}
    if request.method=='POST':
        newmonth=Month_form(request.POST)
        if newmonth.is_valid():
            month=newmonth.cleaned_data['month']
            #formatDate = month.strftime("%B")
            print('qwertyuiowertyhjukilsdfghjksdfghjkldfghjkldxcfgvhbjnkml,xdcfgvbhnjkm,xdcfvg'+month)
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
            yearlyreports=Report.objects.all()
            d={'report':yearlyreports}            
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)

def custom_report(request):
    customform=Custom_form()
    d={'getdate':customform}
    if request.method=='POST':
        newcustom=Custom_form(request.POST)
        if newcustom.is_valid():
            day1=newcustom.cleaned_data['from_date']
            day2=newcustom.cleaned_data['to_date']
            itemlist=newcustom.cleaned_data['items']
            Report.objects.all().delete()
            l=[]
            for i in itemlist:
                orderobj=Order.objects.filter(Q(date__gte=day1)&Q(date__lte=day2)&Q(item=i))
                l.extend(orderobj)
            
            for i in range(0,len(l)-1):
                for j in range(0,len(l)-1):
                    if l[j].date>l[j+1].date:
                        l[j],l[j+1]=l[j+1],l[j]

            d={'report':l}
            return render(request,'RECORDS.HTML',d)
    return render(request,'dateform.html',d)

def addMenuItem(request):
    additem=Menu_item()
    d={'getdate':additem}
    if request.method=='POST':
        itemobj=Menu_item(request.POST)
        if itemobj.is_valid():
            item=itemobj.cleaned_data['item']
            item=item.upper()
            price=itemobj.cleaned_data['price']
            newitem=Menu.objects.create(item=item,price=price)
            newitem.save()
            d={'newitem':newitem}
            
    return render(request,'dateform.html',d)