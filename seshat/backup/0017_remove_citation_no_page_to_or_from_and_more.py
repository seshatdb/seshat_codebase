# Generated by Django 4.0.3 on 2022-08-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_citation_no_page_from_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='citation',
            name='No_PAGE_TO_OR_FROM',
        ),
        migrations.AddConstraint(
            model_name='citation',
            constraint=models.UniqueConstraint(condition=models.Q(('page_to__isnull', True), ('page_from__isnull', True), _connector='OR'), fields=('ref', 'page_to', 'page_from'), name='No_PAGE_TO_OR_FROM'),
        ),
    ]
