# Generated by Django 4.0.3 on 2023-05-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0053_alter_power_transition_polity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power_transition',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]