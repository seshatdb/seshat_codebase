# Generated by Django 4.0.3 on 2023-05-29 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_polity_home_nga'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citation',
            options={'ordering': ['-modified_date']},
        ),
    ]
