from django import forms
from django.contrib.auth.models import User


class Login(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
    def __init__(self,*args,**kwargs):
        super(Login,self).__init__(*args,**kwargs)


class Index(forms.Form):
    url=forms.CharField(max_length=200)
    min=forms.CharField(max_length=3)    
    
    # class Meta:
    #     fields=["url","min"]
    # def __init__(self,*args,**kwargs):
    #     super(Output,self).__init__(*args,**kwargs)