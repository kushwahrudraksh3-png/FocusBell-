from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages
from django.utils import timezone
from . models import *
from django.db.models import Q

# Create your views here.
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    pending_tasks = tasks.filter(status='pending').count()   
    complete_tasks = tasks.filter(status='completed').count()
    today = timezone.localdate()
    overdue_tasks_count = tasks.filter(status='pending', due_date__lt=today).count()
    today_pending_tasks = tasks.filter(status='pending', due_date=today).count()
    
    todays_tasks = tasks.filter(user= request.user, status='pending',  due_date=today)
    upcoming_tasks = tasks.filter(user= request.user, status='pending', due_date__gt=today)
    overdue_tasks = tasks.filter(user= request.user, status='pending', due_date__lt=today)
    
    context = {
        'total_tasks':total_tasks,
        'pending_tasks':pending_tasks,
        'complete_tasks': complete_tasks,
        'overdue_tasks_count': overdue_tasks_count,
        'today_pending_tasks': today_pending_tasks,
        'todays_tasks': todays_tasks,
        'upcoming_tasks': upcoming_tasks,
        'overdue_tasks': overdue_tasks,
    }
    return render(request, 'dashboard.html', context)



@login_required
def task_list(request):
    
    today = timezone.localdate()
    
    search = request.GET.get("search")
    status = request.GET.get("status")
    priority = request.GET.get("priority")
    date_filter = request.GET.get("date")
    
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )
        
    # status filter 

    if status == "pending":
        tasks = tasks.filter(status="pending")

    elif status == "completed":
        tasks = tasks.filter(status="completed")

    elif status == "overdue":
        tasks = tasks.filter(status="pending", due_date__lt=today)
    
    
    # priority filter 
    if priority:
        tasks = tasks.filter(priority=priority)
    
    
    # date filter 
    if date_filter == "today":
        tasks = tasks.filter(due_date=today)

    elif date_filter == "upcoming":
        tasks = tasks.filter(due_date__gt=today)

    elif date_filter == "overdue":
        tasks = tasks.filter(
            due_date__lt=today,
            status="pending"
        )
    
    
    overdue_tasks = tasks.filter(user=request.user, status='pending', due_date__lt=today)
    pending_tasks = tasks.filter(user=request.user, status='pending', due_date__gte=today)
    
    
    
    context = {
        'tasks':tasks,
        'overdue_tasks': overdue_tasks,
        'pending_tasks': pending_tasks,             
    }
    return render(request, 'task_list.html', context)


@login_required
def add_task(request):

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        reminder_before = request.POST.get('reminder_before')
        alarm_enabled = True if request.POST.get('alarm_enabled') == 'on' else False
        
        
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            due_time=due_time,
            reminder_before=reminder_before,
            alarm_enabled=alarm_enabled,
            
        )
        return redirect('task_list')
    return render(request, 'add_task.html')


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.due_date = request.POST.get('due_date')
        task.due_time = request.POST.get('due_time')
        task.reminder_before = request.POST.get('reminder_before')
        task.alarm_enabled = True if request.POST.get('alarm_enabled')=="on" else False

        
        task.save()
        return redirect('dashboard')
    context = {
        'task':task,
    }
    
    return render(request, 'edit_task.html', context)


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id , user=request.user)
    task.delete()
    next_page = request.GET.get("next")

    if next_page == "dashboard":
        return redirect("dashboard")

    return redirect("task_list")




@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    
    task.status = 'completed'
    task.save()
    
    next_page = request.GET.get("next")

    if next_page == "dashboard":
        return redirect("dashboard")

    return redirect("task_list")
    





@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    today = timezone.localdate()

    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    
    if request.method == "POST":
        user = request.user

        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        profile_image = request.FILES.get("profile_picture")

        if profile_image:
            profile.profile_image = profile_image

        user.save()
        profile.save()

        return redirect("profile")

    context = {
        "profile": profile,
        'total_tasks':total_tasks,
        'completed_tasks':completed_tasks,
    }

    return render(request, "edit_profile.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")
        
        user = request.user
        
        if not user.check_password(old_password):
            messages.error(request, "Old password is incorrect")
            return redirect('change_password')
        
        if new_password1 != new_password2:
            messages.error(request, "New password and confirm password do not match")
            
        user.set_password(new_password1)
        user.save()
        
        update_session_auth_hash(request, user)
        
        messages.success(request, "Password changed successfully.")
        return redirect('profile')
    
    
    return render(request, 'change_password.html')



@login_required
def profile(request):

    today = timezone.localdate()

    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(status='completed').count()

    pending_tasks = tasks.filter(status='pending').count()

    overdue_tasks = tasks.filter(status='pending',due_date__lt=today).count()

    recent_completed_tasks = tasks.filter(status='completed').order_by('-updated_at')[:5]

    profile, created = Profile.objects.get_or_create(
    user=request.user
)

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'recent_completed_tasks': recent_completed_tasks,
        'profile':profile,
    }

    return render(request, 'profile.html', context)