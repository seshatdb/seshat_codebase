# Generated by Django 4.0.3 on 2022-11-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_capital_is_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capital',
            options={'ordering': ['is_verified']},
        ),
        migrations.AlterField(
            model_name='capital',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='capital',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
        ),
    ]