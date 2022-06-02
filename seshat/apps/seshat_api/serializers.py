from django.contrib.auth.models import User, Group
from rest_framework import serializers
from seshat.apps.crisisdb.models import Population, Land_taxes_collected, Land_yield, Total_tax, Total_economic_output, Total_revenue, Diding_taxes, Salt_tax, Tariff_and_transit, Misc_incomes, Total_expenditure, Balance, Lijin, Maritime_custom, Other_incomes, Revenue_official, Revenue_real, Gdp_total, Gdp_growth_rate, Shares_of_world_gdp, Gdp_per_capita, Rate_of_gdp_per_capita_growth, Wages, Annual_wages, Rate_of_return, Famine_event, Disease_event, Jinshi_degrees_awarded, Examination, Taiping_rebellion, Worker_wage
from .models import Album
from ..core.models import Polity, Reference, Section, Subsection, VariableHierarchy


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'title', 'year', 'creator', 'zotero_link', 'long_name']


# class FamineSerializer(serializers.ModelSerializer):
#     politys = serializers.HyperlinkedIdentityField(read_only=True)

#     class Meta:
#         model = Famine_event
#         fields = ('longitude', 'latitude', 'elevation', 'politys')


class Land_taxes_collectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land_taxes_collected
        fields = ['year_from', 'year_to', 'land_taxes_collected', 'tag']


class Land_yieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land_yield
        fields = ['year_from', 'year_to', 'land_yield', 'tag']


class Total_taxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_tax
        fields = ['year_from', 'year_to',
                  'total_amount_of_taxes_collected', 'tag']


class Total_economic_outputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_economic_output
        fields = ['year_from', 'year_to', 'total_economic_output', 'tag']


class Total_revenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_revenue
        fields = ['year_from', 'year_to', 'total_revenue', 'tag']


class Diding_taxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diding_taxes
        fields = ['year_from', 'year_to', 'total_revenue', 'tag']


class Salt_taxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salt_tax
        fields = ['year_from', 'year_to', 'salt_tax', 'tag']


class Tariff_and_transitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff_and_transit
        fields = ['year_from', 'year_to', 'tariff_and_transit', 'tag']


class Misc_incomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misc_incomes
        fields = ['year_from', 'year_to', 'misc_incomes', 'tag']


class Total_expenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_expenditure
        fields = ['year_from', 'year_to', 'total_expenditure', 'tag']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['year_from', 'year_to', 'balance', 'tag']


class LijinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lijin
        fields = ['year_from', 'year_to', 'lijin', 'tag']


class Maritime_customSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maritime_custom
        fields = ['year_from', 'year_to', 'maritime_custom', 'tag']


class Other_incomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other_incomes
        fields = ['year_from', 'year_to', 'other_incomes', 'tag']


class Revenue_officialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue_official
        fields = ['year_from', 'year_to', 'revenue_official', 'tag']


class Revenue_realSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue_real
        fields = ['year_from', 'year_to', 'revenue_real', 'tag']


class Gdp_totalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gdp_total
        fields = ['year_from', 'year_to', 'GDP_total', 'tag']


class Gdp_growth_rateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gdp_growth_rate
        fields = ['year_from', 'year_to', 'GDP_growth_rate', 'tag']


class Shares_of_world_gdpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shares_of_world_gdp
        fields = ['year_from', 'year_to', 'shares_of_world_GDP', 'tag']


class Gdp_per_capitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gdp_per_capita
        fields = ['year_from', 'year_to', 'GDP_per_capita', 'tag']


class Rate_of_gdp_per_capita_growthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate_of_gdp_per_capita_growth
        fields = ['year_from', 'year_to',
                  'rate_of_GDP_per_capita_growth', 'tag']


class WagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wages
        fields = ['year_from', 'year_to', 'wages', 'tag']


class Annual_wagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annual_wages
        fields = ['year_from', 'year_to', 'annual_wages',
                  'job_category', 'job_description', 'tag']


class Rate_of_returnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate_of_return
        fields = ['year_from', 'year_to', 'rate_of_return',
                  'job_category', 'job_description', 'tag']


class Famine_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famine_event
        fields = ['year_from', 'year_to', 'famine_event', 'latitude', 'longitude',
                  'elevation', 'sub_category', 'magnitude', 'duration', 'tag']


class Disease_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease_event
        fields = ['year_from', 'year_to', 'disease_event', 'latitude',
                  'longitude', 'elevation', 'sub_category', 'magnitude', 'duration', 'tag']


class Jinshi_degrees_awardedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jinshi_degrees_awarded
        fields = ['year_from', 'year_to', 'jinshi_degrees_awarded',
                  'emperor', 'population_in_year_x', 'tag']


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ['year_from', 'year_to', 'examination', 'no_of_participants', 'degrees_awarded',
                  'passing_ratio', 'place', 'ratio_examiner_per_candidate', 'no_of_examiners', 'tag']


class Taiping_rebellionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taiping_rebellion
        fields = ['year_from', 'year_to', 'taiping_rebellion', 'rebel', 'place',
                  'ethnic_composition', 'family_background', 'role', 'rank', 'civil_examination', 'tag']


class Worker_wageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker_wage
        fields = ['year_from', 'year_to', 'worker_wage', 'area', 'unskilled_construction', 'skilled_construction',
                  'number_of_districts_with_available_data', 'unskilled_arms_manufacturer', 'population_in_millions_in_1787', 'tag']

# Section and Subsection Organizers


class SectionSerializer(serializers.ModelSerializer):
    subsections = serializers.StringRelatedField(many=True,)

    class Meta:
        model = Section
        fields = ['name',
                  'subsections']

# class SectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Section
#         fields = ['name', ]


class PolitySerializer(serializers.ModelSerializer):
    #crisisdb_gdp_per_capita_related = serializers.StringRelatedField(many=True,)
    crisisdb_land_taxes_collected_related = Land_taxes_collectedSerializer(
        many=True, read_only=True)
    crisisdb_land_yield_related = Land_yieldSerializer(
        many=True, read_only=True)
    crisisdb_total_tax_related = Total_taxSerializer(many=True, read_only=True)
    crisisdb_total_economic_output_related = Total_economic_outputSerializer(
        many=True, read_only=True)
    crisisdb_total_revenue_related = Total_revenueSerializer(
        many=True, read_only=True)
    crisisdb_diding_taxes_related = Diding_taxesSerializer(
        many=True, read_only=True)
    crisisdb_salt_tax_related = Salt_taxSerializer(many=True, read_only=True)
    crisisdb_tariff_and_transit_related = Tariff_and_transitSerializer(
        many=True, read_only=True)
    crisisdb_misc_incomes_related = Misc_incomesSerializer(
        many=True, read_only=True)
    crisisdb_total_expenditure_related = Total_expenditureSerializer(
        many=True, read_only=True)
    crisisdb_balance_related = BalanceSerializer(many=True, read_only=True)
    crisisdb_lijin_related = LijinSerializer(many=True, read_only=True)
    crisisdb_maritime_custom_related = Maritime_customSerializer(
        many=True, read_only=True)
    crisisdb_other_incomes_related = Other_incomesSerializer(
        many=True, read_only=True)
    crisisdb_revenue_official_related = Revenue_officialSerializer(
        many=True, read_only=True)
    crisisdb_revenue_real_related = Revenue_realSerializer(
        many=True, read_only=True)
    crisisdb_gdp_total_related = Gdp_totalSerializer(many=True, read_only=True)
    crisisdb_gdp_growth_rate_related = Gdp_growth_rateSerializer(
        many=True, read_only=True)
    crisisdb_shares_of_world_gdp_related = Shares_of_world_gdpSerializer(
        many=True, read_only=True)
    crisisdb_gdp_per_capita_related = Gdp_per_capitaSerializer(
        many=True, read_only=True)
    crisisdb_rate_of_gdp_per_capita_growth_related = Rate_of_gdp_per_capita_growthSerializer(
        many=True, read_only=True)
    crisisdb_wages_related = WagesSerializer(many=True, read_only=True)
    crisisdb_annual_wages_related = Annual_wagesSerializer(
        many=True, read_only=True)
    crisisdb_rate_of_return_related = Rate_of_returnSerializer(
        many=True, read_only=True)
    crisisdb_famine_event_related = Famine_eventSerializer(
        many=True, read_only=True)
    crisisdb_disease_event_related = Disease_eventSerializer(
        many=True, read_only=True)
    crisisdb_jinshi_degrees_awarded_related = Jinshi_degrees_awardedSerializer(
        many=True, read_only=True)
    crisisdb_examination_related = ExaminationSerializer(
        many=True, read_only=True)
    crisisdb_taiping_rebellion_related = Taiping_rebellionSerializer(
        many=True, read_only=True)
    crisisdb_worker_wage_related = Worker_wageSerializer(
        many=True, read_only=True)

    class Meta:
        model = Polity
        fields = ['id', 'name', 'start', 'end',
                  'crisisdb_land_taxes_collected_related', 'crisisdb_land_yield_related', 'crisisdb_total_tax_related', 'crisisdb_total_economic_output_related', 'crisisdb_total_revenue_related', 'crisisdb_diding_taxes_related', 'crisisdb_salt_tax_related', 'crisisdb_tariff_and_transit_related', 'crisisdb_misc_incomes_related', 'crisisdb_total_expenditure_related', 'crisisdb_balance_related', 'crisisdb_lijin_related', 'crisisdb_maritime_custom_related', 'crisisdb_other_incomes_related', 'crisisdb_revenue_official_related', 'crisisdb_revenue_real_related', 'crisisdb_gdp_total_related', 'crisisdb_gdp_growth_rate_related', 'crisisdb_shares_of_world_gdp_related', 'crisisdb_gdp_per_capita_related', 'crisisdb_rate_of_gdp_per_capita_growth_related', 'crisisdb_wages_related', 'crisisdb_annual_wages_related', 'crisisdb_rate_of_return_related', 'crisisdb_famine_event_related', 'crisisdb_disease_event_related', 'crisisdb_jinshi_degrees_awarded_related', 'crisisdb_examination_related', 'crisisdb_taiping_rebellion_related', 'crisisdb_worker_wage_related']

#     def create(self, validated_data):
#         return Polity.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.Famines = validated_data
#         return instance


# class FullPolitySerializer(serializers.ModelSerializer):
#     politys = PolitySerializer(source='salt_tax_related')

#     class Meta:
#         model =


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
