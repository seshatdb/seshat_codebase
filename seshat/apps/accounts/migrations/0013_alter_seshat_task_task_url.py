# Generated by Django 4.0.3 on 2022-10-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_seshat_task_task_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seshat_task',
            name='task_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
