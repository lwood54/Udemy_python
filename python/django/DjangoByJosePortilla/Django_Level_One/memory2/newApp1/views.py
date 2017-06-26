from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    indx_html = {'ins_indx1': "Test, Test, 1,2,1,2"}
    return render(request,'newApp1/index.html',context=indx_html)
