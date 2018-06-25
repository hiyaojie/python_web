from django import forms
from .models import *

class MyForm(forms.ModelForm):
    # sales = forms.ModelChoiceField(label='销售员',queryset=CodeDic.objects.filter(type='sales'),initial='sales')
    # province = forms.ModelChoiceField(label='省份', queryset=CodeDic.objects.filter(type='province'))
    city = forms.ModelChoiceField(label='城市',queryset=CodeDic.objects.filter(type='city'),initial='sales')
    # customer_source = forms.ModelChoiceField(label='客户来源',queryset=CodeDic.objects.filter(type='cus_source'),initial='sales')
    # useage = forms.ModelChoiceField(label='用途',queryset=CodeDic.objects.filter(type='usage'),initial='sales')
    useage_detail = forms.ModelChoiceField(label='用途细分',queryset=CodeDic.objects.filter(type='usage_detail'),initial='sales')
    class Meta:
        model = Order
        exclude =('id',)