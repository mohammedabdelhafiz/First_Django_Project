from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index),
    path('blogs',views.createuser),
    path('blogs/create',views.createuser),
    path('blogs/<int:number>',views.showw),
    path('blogs/<int:number>/edit',views.show),


]
