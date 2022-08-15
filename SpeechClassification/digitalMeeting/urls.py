from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'digitalMeeting'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/savedit/', views.savedit, name='savedit'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('savecreate/', views.savecreate, name='savecreate'),
    path('<int:id>/delete/', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

