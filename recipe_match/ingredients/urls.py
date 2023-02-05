from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('output/<str:url>/<int:min>',views.output,name='output'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='loginpage'),
    path('output/<str:url>/<int:min>/output_more',views.output_more,name='output_more'),
]