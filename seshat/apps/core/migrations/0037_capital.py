# Generated by Django 4.0.3 on 2022-11-24 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_nga_world_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_country', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, max_digits=16, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, max_digits=16, null=True)),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('url_on_the_map', models.URLField(blank=True, null=True)),
                ('polity_cap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polity_caps', to='core.polity')),
            ],
        ),
    ]
