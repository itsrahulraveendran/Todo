# Generated by Django 4.2.2 on 2023-07-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='discription',
            field=models.TextField(default='write discriptions'),
            preserve_default=False,
        ),
    ]
