from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('m',views.momo,name='momo'),
    path('<str:name>',views.greet,name='greet') 

]