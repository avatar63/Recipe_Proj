from django.shortcuts import render
from django.template import loader
from .models import temp_url
import urllib.parse

from django.http import HttpResponse, HttpResponseRedirect
from .ingredient_code.recipes import *

#Create your views here.

def index(request):
    if request.method == "POST":
        data = str(request.POST['url']).replace("/","_")
        data2= int(request.POST['min'])
        return HttpResponseRedirect("output/"+data+"/"+str(data2))

    return render(request,'index.html')

def output(request,url,min):    
    url=url.replace("_","/")
    ob = recipes(url,'')
    ob.dish_gen()
    dish_url=ob.url_gen()

    ob.dish_recipe(dish_url)
    ob.comparison_analysis()
    dict_data=ob.compared(int(min))
    final_data=dict_data # list of dictionaries 
    context ={
        'final_data' : final_data,
    }
    return render(request,'output.html',context)
