from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from .ingredient_code.recipes import *

# Create your views here.

def index(request):
    template = loader.get_template('index.html')

    return HttpResponse(template.render({},request))

def output(request,url='https://www.budgetbytes.com/category/recipes/meat/chicken/chicken-thighs/',min=2):
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
    template=loader.get_template('output.html')
    return HttpResponse(template.render(context,request))
    #return url, min
