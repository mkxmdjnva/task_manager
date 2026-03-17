from django.shortcuts import render , redirect,  get_object_or_404
from main.models import Task 
import main.forms as forms
from django.contrib.auth.decorators import login_required
from main.models import UserPrivacy
# Create your views here.
 
@login_required
def settings_view(request):
    return render(request, 'settings.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})



def home(request):
    return render(request, "index.html")

def vazifalar(request):
    return render(request, "vazifalar.html")

def kalendar(request):
    return render(request, "kalendar.html")

def statistics(request):
    return render(request, "statistics.html")

def settings(request):
    return render(request, "settings.html")

def view(request):
    return render(request, "view.html")

def yangi_vazifa(request):
   if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('description')
        deadline = request.POST.get('deadline')
        
        if title:
            Task.objects.create(title=title,
                                 description=desc, 
                                 deadline=deadline,
                                 user=request.user
                                 )
        return redirect('home')
   return render(request, "yangi_vazifa.html")

def vazifalarni_qidirish(request):
    search = request.GET.get("search")
    task_list = Task.objects.all()
    if search:
        recipe_list = recipe_list.filter(title__icontains=search)
        
    context = {
        "task": task_list
    }
    return render(request, "index.html", context)


def task_list_view(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})


@login_required
def privacy_settings(request):
    privacy, created = UserPrivacy.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        privacy.is_private = request.POST.get('is_private') == 'on'
        privacy.show_online = request.POST.get('show_online') == 'on'
        privacy.allow_search = request.POST.get('allow_search') == 'on'
        
        privacy.save()
        return redirect('privacy_view') 

    return render(request, 'privacy.html', {'privacy': privacy})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.name = request.POST.get('name')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('task_list')
    return render(request, 'update.html', {'task': task})