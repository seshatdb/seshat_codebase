# Generated by Django 4.0.3 on 2022-09-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_seshat_expert_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seshat_expert',
            name='role',
            field=models.CharField(blank=True, choices=[('Seshat Admin', 'Seshat Admin'), ('RA', 'RA'), ('Seshat Expert', 'Seshat Expert')], max_length=60, null=True),
        ),
    ]
