# Generated by Django 4.0.3 on 2022-09-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_seshat_expert_role'),
        ('crisisdb', '0025_alter_arable_land_curator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arable_land',
            name='curator',
        ),
        migrations.AddField(
            model_name='arable_land',
            name='curator',
            field=models.ManyToManyField(blank=True, null=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='accounts.seshat_expert'),
        ),
    ]
