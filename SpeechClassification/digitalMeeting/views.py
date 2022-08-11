from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting
from django.utils import timezone


def index(request):

    meeting_list = Meeting.objects.all()

    context = {'meeting_list': meeting_list}

    return render(request, 'digitalMeeting/index.html', context)