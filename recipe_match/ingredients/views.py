from django.shortcuts import render,redirect
from django.template import loader
import urllib.parse
from .forms import Index#,Login
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
            return redirect("login")
    else:
        form=UserCreationForm()
    return render(request,'register.html',{"form":form})


def index(request):
    form=Index()
    print(request.user)
    if request.method == "POST":
        data = dict(request.POST)
        print(data)
        data1 = data["ingredients"]
        data2 = data["minimum_recipes"][0]
        print(data2)
        temp=[]
        for i in data1:
            temp.append(i)
        data1 = "~".join(temp)
        return HttpResponseRedirect("/ingredients/output/"+str(data1)+"/"+(data2))

    return render(request,'index.html',{"form":form})

def output(request,ingredients,minimum_recipes):
    temp_list=ingredients.split("~")
    print(temp_list)
    data=",".join(temp_list)
    print(data)
    ob = recipe_parser("fbb7be320f9842a9ad38be90a1e8e288")
    data_dict=ob.recipes_search(data,minimum_recipes)
    final_data=ob.final_data(data_dict)
    # print(final_data)
    name = request.user
    context ={
        'final_data' : final_data,
        'name' : name,
    }
    return render(request,'output.html',context)


def know_more(request,id):
    ob=recipe_parser("fbb7be320f9842a9ad38be90a1e8e288")
    dish_data = ob.recipeinformation(id)
    instructions = dish_data["analyzedInstructions"]
    name = request.user
    context = {
        'dish_data':dish_data,
        'instructions':instructions,
        'name':name
    }
    return render(request,'know_more.html',context)

def profile(request):
    name = request.user

    context = {
        "name":name
    }
    return render(request,"registration/profile.html",context=context)
