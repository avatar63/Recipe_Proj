from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('output/<ingredients>',views.output,name='output'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='loginpage'),
    
]