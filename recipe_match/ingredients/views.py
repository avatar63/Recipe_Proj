from django.shortcuts import render
from django.template import loader
import urllib.parse

from django.http import HttpResponse, HttpResponseRedirect
from .ingredient_code.recipes import *

# Create your views here.

def index(request):
    if request.method == "POST":
        data = str(request.POST['url'])
        data2= int(request.POST['min'])
        data=urllib.parse.quote(data,safe='')
        return HttpResponseRedirect("output/"+data+"/"+data2)

    return render(request,'index.html')

def output(request,url,min):
    ob = recipes(url,'')
    ob.dish_gen()
    dish_url=ob.url_gen()

    ob.dish_recipe(dish_url)
    ob.comparison_analysis()
    final_data=list(ob.compared(min)) 
    print(final_data)
    context ={
        'final_data' : final_data,
    }
    # return "Hello World!" 
    return render(request,'output.html',)
