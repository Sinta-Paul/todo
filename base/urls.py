from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('create/',views.createtask,name="createtask"),
    path('delete/<str:pk>/',views.deletetask,name="deletetask"),
]