from celery import shared_task
from django.utils import timezone
from datetime import datetime, timedelta
from .whatsapp import send_whatsapp_message
from .models import Task


@shared_task
def check_due_tasks():
    now = timezone.localtime()
    today = now.date()
    current_time = now.time()

    tasks = Task.objects.filter(
        status="pending",
        due_date=today,
        alarm_enabled=True,
        is_reminded=False
    )
    print("Total tasks found:", tasks.count())

    for task in tasks:
        task_datetime = datetime.combine(task.due_date, task.due_time)

        reminder_time = task_datetime - timedelta(minutes=task.reminder_before)
        
            

        print("Task:", task.title)
        print("Due Time:", task.due_time)
        print("Reminder Before:", task.reminder_before)
        print("Current Time:", current_time)
        print("Reminder Time:", reminder_time.time())
        print("Is Reminded:", task.is_reminded)
        print("---------------------")

        if reminder_time.time().hour == current_time.hour and reminder_time.time().minute == current_time.minute:
            # print(f"Reminder: {task.title}")
            message = f"""🔔 FocusBell Reminder

            Task: {task.title}
            Time: {task.due_time}

            Your task is starting soon.
            """ 
            send_whatsapp_message(message)
            task.is_reminded = True
            task.save()