# Generated by Django 4.1.7 on 2023-06-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_remove_students_profile_pic_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.FileField(default='default.png', upload_to='profiles/'),
        ),
    ]
