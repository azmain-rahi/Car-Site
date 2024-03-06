from django.contrib import admin
from django.urls import path
from cars import views

app_name ='cars'

urlpatterns = [
    path('list/',views.list_view,name='list'),
    path('add/',views.add_view,name='add'),
    path('delete/',views.delete_view,name='delete'),
    path('<str:topic>/',views.delete_view,name='not_found')
]
