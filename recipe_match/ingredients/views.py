from django.shortcuts import render
from django.template import loader
from .models import temp_url
import urllib.parse

from django.http import HttpResponse, HttpResponseRedirect
from .ingredient_code.recipes import *

# Create your views here.

def index(request):
    if request.method == "POST":
        data = str(request.POST['url'])
        
        # temp=temp_url(data)
        # temp.save()
        data2= int(request.POST['min'])
        data=urllib.parse.quote(data,safe='')
        return HttpResponseRedirect("output/"+data+"/"+str(data2))

    return render(request,'index.html')

def output(request,url,min):
    url_dict={"Chicken Breast":"https://www.budgetbytes.com/category/recipes/meat/chicken/chicken-breasts/","Chicken Thigh":"https://www.budgetbytes.com/category/recipes/meat/chicken/chicken-thighs/","Baked Chicken":"https://www.budgetbytes.com/category/recipes/meat/chicken/chicken-baked/","Quick Chicken":"https://www.budgetbytes.com/category/recipes/meat/chicken/quick-chicken/","Chicken Wing":"https://www.budgetbytes.com/category/recipes/meat/chicken/chicken-wings/","Chicken Salad":"https://www.budgetbytes.com/category/recipes/meat/chicken/chicken-salad/","Quick Pasta":"https://www.budgetbytes.com/category/recipes/pasta/quick-pasta/","Vegetarian Pasta":"https://www.budgetbytes.com/category/recipes/pasta/vegetarian-pastas/","Chicken Pasta":"https://www.budgetbytes.com/category/recipes/pasta/chicken-pasta/","Tofu":"https://www.budgetbytes.com/category/recipes/pasta/chicken-pasta/","Vegan":"https://www.budgetbytes.com/category/recipes/vegetarian/vegan/","Chicken Slow Cooker":"https://www.budgetbytes.com/category/recipes/slow-cooker/slow-cooker-chicken/","Pork Slow Cooker":"https://www.budgetbytes.com/category/recipes/slow-cooker/slow-cooker-pork/","Slow Cooker Soup":"https://www.budgetbytes.com/category/recipes/soup/slow-cooker-soup/","Vegetarian Slow Cooker":"https://www.budgetbytes.com/category/recipes/slow-cooker/slow-cooker-vegetarian/","Savory Breakfast":"https://www.budgetbytes.com/category/recipes/breakfast/savory-breakfast-recipes/","Sweet Breakfast":"https://www.budgetbytes.com/category/recipes/breakfast/sweet-breakfast-recipes/","Cold Breakfast":"https://www.budgetbytes.com/category/recipes/breakfast/cold-breakfast-recipes/","Hot Breakfast":"https://www.budgetbytes.com/category/recipes/breakfast/hot-breakfast-recipes/","Breakfast Baked Goods":"https://www.budgetbytes.com/category/recipes/breakfast/breakfast-baked-goods/","Egg":"https://www.budgetbytes.com/category/recipes/breakfast/eggs-breakfast/","Oat":"https://www.budgetbytes.com/category/recipes/breakfast/oats/","Chicken Soup":"https://www.budgetbytes.com/category/recipes/soup/chicken-soup/","Vegetarian Soup":"https://www.budgetbytes.com/category/recipes/soup/soup-vegetarian/"}

    
    url=url_dict[url]
    ob = recipes(url,'')
    ob.dish_gen()
    dish_url=ob.url_gen()

    ob.dish_recipe(dish_url)
    ob.comparison_analysis()
    dict_data=ob.compared(int(min))
    final_data=dict_data #a list of dictionaries 
    context ={
        'final_data' : final_data,
    }
    # return "Hello World!" 
    return render(request,'output.html',context)