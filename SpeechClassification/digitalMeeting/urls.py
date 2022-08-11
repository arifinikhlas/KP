from django.urls import path

from . import views

app_name = 'digitalMeeting'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/savedit/', views.savedit, name='savedit'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]