# Generated by Django 4.0.3 on 2022-10-21 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_seshatcommentpart_citation_index'),
        ('accounts', '0013_alter_seshat_task_task_url'),
        ('crisisdb', '0036_alter_agricultural_population_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease_outbreak',
            name='elevation',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='disease_outbreak',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='disease_outbreak',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='external_conflict_side',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='gdp_per_capita',
            name='gdp_per_capita',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='internal_conflict',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='military_expense',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.CreateModel(
            name='Human_sacrifice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Evidenced'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5)),
                ('name', models.CharField(default='Human_sacrifice', max_length=100)),
                ('human_sacrifice', models.CharField(choices=[('U', 'U'), ('A;P', 'A;P'), ('P*', 'P*'), ('P', 'P'), ('A~P', 'A~P'), ('A', 'A'), ('A*', 'A*'), ('P~A', 'P~A')], max_length=500)),
                ('citations', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.seshatcomment')),
                ('curator', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='accounts.seshat_expert')),
                ('polity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity')),
            ],
            options={
                'verbose_name': 'Human_sacrifice',
                'verbose_name_plural': 'Human_sacrifices',
            },
        ),
    ]
