# Generated by Django 4.0.3 on 2023-01-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_alter_polity_alternate_religion_tag_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polity_alternate_religion',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_alternate_religion', 'verbose_name_plural': 'Polity_alternate_religions'},
        ),
        migrations.AlterModelOptions(
            name='polity_alternate_religion_family',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_alternate_religion_family', 'verbose_name_plural': 'Polity_alternate_religion_families'},
        ),
        migrations.AlterModelOptions(
            name='polity_alternate_religion_genus',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_alternate_religion_genus', 'verbose_name_plural': 'Polity_alternate_religion_genus'},
        ),
        migrations.AlterModelOptions(
            name='polity_alternative_name',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_alternative_name', 'verbose_name_plural': 'Polity_alternative_names'},
        ),
        migrations.AlterModelOptions(
            name='polity_capital',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_capital', 'verbose_name_plural': 'Polity_capitals'},
        ),
        migrations.AlterModelOptions(
            name='polity_degree_of_centralization',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_degree_of_centralization', 'verbose_name_plural': 'Polity_degree_of_centralizations'},
        ),
        migrations.AlterModelOptions(
            name='polity_duration',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_duration', 'verbose_name_plural': 'Polity_durations'},
        ),
        migrations.AlterModelOptions(
            name='polity_editor',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_editor', 'verbose_name_plural': 'Polity_editors'},
        ),
        migrations.AlterModelOptions(
            name='polity_expert',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_expert', 'verbose_name_plural': 'Polity_experts'},
        ),
        migrations.AlterModelOptions(
            name='polity_language',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_language', 'verbose_name_plural': 'Polity_languages'},
        ),
        migrations.AlterModelOptions(
            name='polity_language_genus',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_language_genus', 'verbose_name_plural': 'Polity_language_genus'},
        ),
        migrations.AlterModelOptions(
            name='polity_linguistic_family',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_linguistic_family', 'verbose_name_plural': 'Polity_linguistic_families'},
        ),
        migrations.AlterModelOptions(
            name='polity_original_name',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_original_name', 'verbose_name_plural': 'Polity_original_names'},
        ),
        migrations.AlterModelOptions(
            name='polity_peak_years',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_peak_years', 'verbose_name_plural': 'Polity_peak_years'},
        ),
        migrations.AlterModelOptions(
            name='polity_preceding_entity',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_preceding_entity', 'verbose_name_plural': 'Polity_preceding_entities'},
        ),
        migrations.AlterModelOptions(
            name='polity_relationship_to_preceding_entity',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_relationship_to_preceding_entity', 'verbose_name_plural': 'Polity_relationship_to_preceding_entities'},
        ),
        migrations.AlterModelOptions(
            name='polity_religion',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_religion', 'verbose_name_plural': 'Polity_religions'},
        ),
        migrations.AlterModelOptions(
            name='polity_religion_family',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_religion_family', 'verbose_name_plural': 'Polity_religion_families'},
        ),
        migrations.AlterModelOptions(
            name='polity_religion_genus',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_religion_genus', 'verbose_name_plural': 'Polity_religion_genus'},
        ),
        migrations.AlterModelOptions(
            name='polity_religious_tradition',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_religious_tradition', 'verbose_name_plural': 'Polity_religious_traditions'},
        ),
        migrations.AlterModelOptions(
            name='polity_research_assistant',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_research_assistant', 'verbose_name_plural': 'Polity_research_assistants'},
        ),
        migrations.AlterModelOptions(
            name='polity_scale_of_supracultural_interaction',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_scale_of_supracultural_interaction', 'verbose_name_plural': 'Polity_scale_of_supracultural_interactions'},
        ),
        migrations.AlterModelOptions(
            name='polity_succeeding_entity',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_succeeding_entity', 'verbose_name_plural': 'Polity_succeeding_entities'},
        ),
        migrations.AlterModelOptions(
            name='polity_supracultural_entity',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_supracultural_entity', 'verbose_name_plural': 'Polity_supracultural_entities'},
        ),
        migrations.AlterModelOptions(
            name='polity_suprapolity_relations',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_suprapolity_relations', 'verbose_name_plural': 'Polity_suprapolity_relations'},
        ),
        migrations.AlterModelOptions(
            name='polity_utm_zone',
            options={'ordering': ['year_from', 'year_to'], 'verbose_name': 'Polity_utm_zone', 'verbose_name_plural': 'Polity_utm_zones'},
        ),
        migrations.AddField(
            model_name='polity_alternate_religion',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion_family',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion_family',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion_genus',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternate_religion_genus',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternative_name',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_alternative_name',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_capital',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_capital',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_degree_of_centralization',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_degree_of_centralization',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_duration',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_duration',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_editor',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_editor',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_expert',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_expert',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_language',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_language',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_language_genus',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_language_genus',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_linguistic_family',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_linguistic_family',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_original_name',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_original_name',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_peak_years',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_peak_years',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_preceding_entity',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_preceding_entity',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_relationship_to_preceding_entity',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_relationship_to_preceding_entity',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion_family',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion_family',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion_genus',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religion_genus',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_religious_tradition',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_religious_tradition',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_research_assistant',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_research_assistant',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_scale_of_supracultural_interaction',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_scale_of_supracultural_interaction',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_succeeding_entity',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_succeeding_entity',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_supracultural_entity',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_supracultural_entity',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_suprapolity_relations',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_suprapolity_relations',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='polity_utm_zone',
            name='drb_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='polity_utm_zone',
            name='expert_reviewed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
