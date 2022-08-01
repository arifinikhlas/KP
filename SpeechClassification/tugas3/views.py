from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.utils import timezone


def index(request):
    message_list = Message.objects.all()

    context = {'message_list': message_list}

    return render(request, 'tugas3/index.html', context)

def save(request):
    if request.method == 'POST' and request.POST['message']:
        message = Message(question_text=request.POST['message'], pub_date = timezone.now())
        message.save()

    return redirect('/tugas3')

def edit(request, id):
    message = get_object_or_404(Message, id=id)

    context = {'message': message}
    
    return render(request, 'tugas3/edit.html', context)

def savedit(request, id):
    message = get_object_or_404(Message, id=id)

    message.question_text = request.POST['message']
    message.pub_date = timezone.now()
    # file.location = request.POST['location']
    message.save()

    return redirect('/tugas3')

def delete(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()

    return redirect('/tugas3')