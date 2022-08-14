from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting
from django.utils import timezone


def index(request):

    meeting_list = Meeting.objects.all()

    context = {'meeting_list': meeting_list, 'keyword':''}

    return render(request, 'digitalMeeting/index.html', context)

def create(request):
    context = {}
    return render(request, 'digitalMeeting/create.html', context)

def savecreate(request):

    if request.method == 'POST':
        meeting = Meeting(
            title = request.POST['title'],
            description = request.POST['description'],
            thumbnail = request.POST['thumbnail'],
            pub_date = timezone.now())
        meeting.save()

    return redirect('/digitalMeeting')

def edit(request, id):
    meeting = get_object_or_404(Meeting, id=id)

    context = {'meeting': meeting}
    
    return render(request, 'digitalMeeting/edit.html', context)

def savedit(request, id):
    meeting = get_object_or_404(Meeting, id=id)

    meeting.title = request.POST['title']
    meeting.description = request.POST['description']
    meeting.thumbnail = request.POST['thumbnail']
    meeting.pub_date = timezone.now()
    # file.location = request.POST['location']
    meeting.save()

    return redirect('/digitalMeeting')

def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)

    context = {'meeting': meeting}
    
    return render(request, 'digitalMeeting/detail.html', context)

def search(request):
    list = Meeting.objects.all()
    keyword = ''
    if(request.method=='POST'):
        keyword = request.POST.get('keyword')
        list = Meeting.objects.filter(title__icontains=keyword)   

    context = {'meeting_list' : list, 'keyword' : keyword}

    return render(request,'digitalMeeting/index.html', context)

def delete(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    meeting.delete()

    return redirect('/digitalMeeting')