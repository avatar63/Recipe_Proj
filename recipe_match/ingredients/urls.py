from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('output/url=/min=',views.output,name='output'),
    path('output/<str:url>/<int:min>',views.output,name='output')
]