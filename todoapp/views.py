from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    '''Renders The Home Page'''
    return render(request, 'index.html')

def index(request):
    '''Renders The Index Page'''
    return render(request, 'index.html')

def user(request):
    '''Renders The User Page'''

    my_tasks = Task.objects.all()
    return render(request, 'users.html', {'my_tasks': my_tasks})

def profile(request):
    '''Renders The Profile Page'''
    return render(request, 'profile.html')

def log(request):
    '''Renders The log Page'''
    return render(request, 'log.html')

def sign(request):
    '''Renders The Sign Page'''
    return render(request, 'sign.html')

def edit(request):
    '''Renders The Edit Page'''
    return render(request, 'edit.html')

def add_task(request):
    '''Adds A Task'''

    if request.method == "POST":
        passed_task = request.POST.get('a_task')
        new_task = Task()
        new_task.name = passed_task
        new_task.save()
    # print(passed_task)
    return redirect('user')

def delete_task(request):
    """Deletes A Task"""

    item_to_delete = request.GET.get('item_to_be_deleted')
    the_item = Task.objects.get(id=item_to_delete)
    the_item.delete()
    return redirect('user')

def edit_task(request):
    """Edits A Task"""

    if request.method == "POST":
        get_task = request.POST.get('task_to_be_edited')
        print(get_task)
        the_id = request.POST.get('the_edit')
        the_edited_item = Task.objects.get(id=the_id)
        the_edited_item.name = get_task
        the_edited_item.save()

    return redirect('user')