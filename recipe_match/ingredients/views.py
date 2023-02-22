from django.shortcuts import render,redirect
from django.template import loader
import urllib.parse
from .forms import Index,Login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,get_user
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse, HttpResponseRedirect
from .spoon.main import recipe_parser
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
        data = data["ingredients"]
        print(data)
        temp=[]
        for i in data:    
            temp.append(i) 
        data = "*".join(temp)
        return HttpResponseRedirect("/ingredients/output/"+str(data))

    return render(request,'index.html',{"form":form})

def output(request,ingredients):
    temp_list=ingredients.split("*")
    print(temp_list)
    data=",".join(temp_list)
    print(data)
    ob = recipe_parser("fbb7be320f9842a9ad38be90a1e8e288")
    data_dict=ob.recipes_search(data)
    final_data=ob.final_data(data_dict)
    # print(final_data)
    context ={
        'final_data' : final_data,
    }
    return render(request,'output.html',context)






