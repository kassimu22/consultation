# tasks.py
from django.core.mail import send_mail
from celery import shared_task
from datetime import datetime, timedelta
from .models import Appointment

@shared_task
def send_reminders():
    # Get appointments that are scheduled within the next 24 hours
    now = datetime.now()
    end_time = now + timedelta(days=1)
    appointments = Appointment.objects.filter(start_time__range=[now, end_time])

    for appointment in appointments:
        lecturer = appointment.lecturer
        lecturer_email = lecturer.email

        # Send reminder to the lecturer
        send_mail(
            'Appointment Reminder',
            f'You have an upcoming appointment with {appointment.student} on {appointment.start_time}',
            'your_email@example.com',
            [lecturer_email],
            fail_silently=False,
        )
