# Generated by Django 4.2.2 on 2023-07-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_remove_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
