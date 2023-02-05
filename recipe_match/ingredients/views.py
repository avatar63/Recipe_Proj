from django.shortcuts import render,redirect
from django.template import loader
import urllib.parse
from .forms import Index,Login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,get_user
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse, HttpResponseRedirect
from .ingredient_code.recipes import *
#USERMODEL, DJANGO


#Create your views here.
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect("loginpage")
    else:
        form=UserCreationForm()
    return render(request,'register.html',{"form":form})
            
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            return redirect("index")

        else:
            return HttpResponse("Login Failed.")

    else:
        form = Login()    
    return (render(request,'loginpage.html',{"form":form}))

def index(request):
    form=Index()
    print(request.user)
    if request.method == "POST":
        data = dict(request.POST)
        print(data)
        data = data["url"]
        temp=[]
        for i in data:
            mod_url=i.replace("/","_")   
            temp.append(mod_url) 
        data = "*".join(temp)
        print(data)
        #data = str(request.POST['url']).replace("/","_")
        data2= int(request.POST['min'])
        return HttpResponseRedirect("output/"+data+"/"+str(data2))

    return render(request,'index.html',{"form":form})

def output(request,url,min):
    temp_list=url.split("*")
    url_list=[]
    for url in temp_list:
        url_list.append(url.replace("_","/"))
    print(url_list)
    ob = recipes(url,'')
    # ob.dish_gen()
    # dish_url=ob.url_gen()
    ob.name_dish(url_list)
    ob.dish_recipe(url_list)
    ob.comparison_analysis()
    dict_data=ob.compared(int(min))
    final_data=dict_data # list of dictionaries 
    context ={
        'final_data' : final_data,
    }
    return render(request,'output.html',context)

def output_more(request,url,min):
    
    url=url.replace("_","/")
    url=url+"page/2"
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






