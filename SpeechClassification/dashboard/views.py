from collections import Counter
from django.shortcuts import render

from dashboard.models import UserTop5, Daily

def index(request):
    user_list = UserTop5.objects.filter().order_by('-points')[:5]
    dalily_list = Daily.objects.all()[:7]
    context = {
        'user_list': user_list,
        'daily_list': dalily_list
    }
    return render(request, 'dashboard/index.html', context)