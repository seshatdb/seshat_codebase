# Generated by Django 4.0.3 on 2022-08-29 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_citation_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='ref',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='citation', to='core.reference'),
        ),
    ]
