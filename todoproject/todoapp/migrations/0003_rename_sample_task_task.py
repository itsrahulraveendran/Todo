# Generated by Django 4.2.2 on 2023-07-16 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_sample_task_delete_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sample_task',
            new_name='Task',
        ),
    ]
