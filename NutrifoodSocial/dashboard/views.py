from django.shortcuts import render

def index(request):

    user_count = 10
    department_count = 10
    division_count = 10
    context = {
        'user_count':user_count,
        'department_count':department_count,
        'division_count':division_count
        }
        
    return render(request, 'dashboard/index.html', context)

