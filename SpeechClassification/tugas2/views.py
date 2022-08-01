from django.shortcuts import render


def index(request):
    return render(request, 'tugas2/index.html')