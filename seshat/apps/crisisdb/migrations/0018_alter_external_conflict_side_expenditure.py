# Generated by Django 4.0.3 on 2022-09-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0017_remove_external_conflict_sides_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='external_conflict_side',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
