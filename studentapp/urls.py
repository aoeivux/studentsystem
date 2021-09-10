from django.urls import path
from . import views

app_name = 'studentapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('response/',views.response,name='response'),
    path('search/',views.search, name='search'),

]
