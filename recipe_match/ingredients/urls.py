from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('output/<str:ingredients>/<int:minimum_recipes>',views.output,name='output'),
    path('food/<str:id>',views.know_more,name='know_more'),
]
