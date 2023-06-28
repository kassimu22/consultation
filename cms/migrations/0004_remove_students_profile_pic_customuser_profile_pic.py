# Generated by Django 4.1.7 on 2023-06-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_appointment_reason_students_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.FileField(default='', upload_to='profiles/'),
        ),
    ]
