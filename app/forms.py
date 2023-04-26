from django import forms
from app.models import *
import datetime

class Order_form(forms.Form):
    form_menu_obj=Menu.objects.all()
    item=forms.ModelChoiceField(form_menu_obj)
    qty=forms.IntegerField(min_value=1)
    
class Date_form(forms.Form):
       date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'})
       )


class Month_form(forms.Form):
       
         months=[(1,'JANUARY'),(2,'FEBRAURY'),(3,'MARCH'),(4,'APRIL'),(5,'MAY'),(6,'JUNE'),(7,'JULY'),(8,'AUGUST'),(9,'SEPTEMBER'),(10,'OCTOBER'),(11,'NOVEMBER'),(12,'DECEMBER')]
         month=forms.ChoiceField(choices=months)
        # month=forms.ChoiceField(widget=forms.widgets.DateInput(format='%M',attrs={'type':'month','placeholder':'mm','class':'form-control'}))
class Year_form(forms.Form):
        years=[(2022,2022),(2023,2023),(2024,2024)]    
        year = forms.ChoiceField(choices=years)

class Custom_form(forms.Form):
        from_date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}))
        to_date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}))
        menuobj=Menu.objects.only('item')
        choicelist=[]
        for i in menuobj:
             if i.item not in choicelist:
                    t=(i.item,i.item)
                    choicelist.append(t)
        items=forms.MultipleChoiceField(widget=forms.widgets.CheckboxSelectMultiple() ,choices=choicelist)

class Menu_item(forms.ModelForm):
       class Meta:
              model=Menu
              fields='__all__'