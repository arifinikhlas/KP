from django.urls import path

from . import views

app_name = 'digitalMeeting'

urlpatterns = [
    path('', views.index, name='index'),

]