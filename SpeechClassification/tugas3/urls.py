from django.urls import path

from . import views

app_name = 'tugas3'

urlpatterns = [
    path('', views.index, name='index'),

    path('save/', views.save, name='save'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/savedit/', views.savedit, name='savedit'),
    path('<int:id>/delete/', views.delete, name='delete'),
]