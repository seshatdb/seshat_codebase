# Generated by Django 4.0.3 on 2022-08-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_reference_options_citation_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citation',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='reference',
            options={'ordering': ['-modified_date']},
        ),
    ]
