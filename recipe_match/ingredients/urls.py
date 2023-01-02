from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('Form/<url>/',views.output,name='output'),
    path('Form/',views.output,name='output')
]