# Generated by Django 4.0.3 on 2022-11-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_capital'),
    ]

    operations = [
        migrations.AddField(
            model_name='capital',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
