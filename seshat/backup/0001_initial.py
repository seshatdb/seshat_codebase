# Generated by Django 4.0.3 on 2022-03-02 11:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('end', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'polity',
                'verbose_name_plural': 'polities',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a book Genre Please...', max_length=200)),
                ('year', models.IntegerField(blank=True, help_text='year of Publication', null=True)),
                ('creator', models.CharField(help_text='Creator of pub', max_length=100)),
                ('zotero_link', models.CharField(help_text='choose the 8-digit Zotero link', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsections', to='core.section')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('polity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countries', to='core.polity')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this particular citation', primary_key=True, serialize=False)),
                ('page_from', models.IntegerField(blank=True, null=True)),
                ('page_to', models.IntegerField(blank=True, null=True)),
                ('ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='citation', to='core.reference')),
            ],
        ),
    ]