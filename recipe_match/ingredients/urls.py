from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('output/<str:ingredients>/<int:minimum_recipes>',views.output,name='output'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='loginpage'),
    path('food/<str:id>',views.know_more,name='know_more')
]