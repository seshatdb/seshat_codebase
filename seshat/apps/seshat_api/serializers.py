
################ Beginning of Serializers Imports (TODO: Make them automatic too)

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from seshat.apps.crisisdb.models import Human_sacrifice, External_conflict, Internal_conflict, External_conflict_side, Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak
from ..core.models import Polity, Reference, Section, Subsection, Variablehierarchy

################ End of Serializers Imports

################ Beginning of Base Serializers
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
        
################ End of Base Serializers
################ Beginning of Serializers Imports

class Human_sacrificeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human_sacrifice
        fields = ['year_from', 'year_to', 'human_sacrifice', 'tag']

class External_conflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = External_conflict
        fields = ['year_from', 'year_to', 'conflict_name', 'tag']

class Internal_conflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internal_conflict
        fields = ['year_from', 'year_to', 'conflict', 'expenditure', 'leader', 'casualty', 'tag']

class External_conflict_sideSerializer(serializers.ModelSerializer):
    class Meta:
        model = External_conflict_side
        fields = ['year_from', 'year_to', 'conflict_id', 'expenditure', 'leader', 'casualty', 'tag']

class Agricultural_populationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agricultural_population
        fields = ['year_from', 'year_to', 'agricultural_population', 'tag']

class Arable_landSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arable_land
        fields = ['year_from', 'year_to', 'arable_land', 'tag']

class Arable_land_per_farmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arable_land_per_farmer
        fields = ['year_from', 'year_to', 'arable_land_per_farmer', 'tag']

class Gross_grain_shared_per_agricultural_populationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gross_grain_shared_per_agricultural_population
        fields = ['year_from', 'year_to', 'gross_grain_shared_per_agricultural_population', 'tag']

class Net_grain_shared_per_agricultural_populationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Net_grain_shared_per_agricultural_population
        fields = ['year_from', 'year_to', 'net_grain_shared_per_agricultural_population', 'tag']

class SurplusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surplus
        fields = ['year_from', 'year_to', 'surplus', 'tag']

class Military_expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Military_expense
        fields = ['year_from', 'year_to', 'conflict', 'expenditure', 'tag']

class Silver_inflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silver_inflow
        fields = ['year_from', 'year_to', 'silver_inflow', 'tag']

class Silver_stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silver_stock
        fields = ['year_from', 'year_to', 'silver_stock', 'tag']

class Total_populationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_population
        fields = ['year_from', 'year_to', 'total_population', 'tag']

class Gdp_per_capitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gdp_per_capita
        fields = ['year_from', 'year_to', 'gdp_per_capita', 'tag']

class Drought_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drought_event
        fields = ['year_from', 'year_to', 'drought_event', 'tag']

class Locust_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locust_event
        fields = ['year_from', 'year_to', 'locust_event', 'tag']

class Socioeconomic_turmoil_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socioeconomic_turmoil_event
        fields = ['year_from', 'year_to', 'socioeconomic_turmoil_event', 'tag']

class Crop_failure_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop_failure_event
        fields = ['year_from', 'year_to', 'crop_failure_event', 'tag']

class Famine_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Famine_event
        fields = ['year_from', 'year_to', 'famine_event', 'tag']

class Disease_outbreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease_outbreak
        fields = ['year_from', 'year_to', 'longitude', 'latitude', 'elevation', 'sub_category', 'magnitude', 'duration', 'tag']
class PolitySerializer(serializers.ModelSerializer):
	crisisdb_human_sacrifice_related = Human_sacrificeSerializer(many=True, read_only=True)
	crisisdb_external_conflict_related = External_conflictSerializer(many=True, read_only=True)
	crisisdb_internal_conflict_related = Internal_conflictSerializer(many=True, read_only=True)
	crisisdb_external_conflict_side_related = External_conflict_sideSerializer(many=True, read_only=True)
	crisisdb_agricultural_population_related = Agricultural_populationSerializer(many=True, read_only=True)
	crisisdb_arable_land_related = Arable_landSerializer(many=True, read_only=True)
	crisisdb_arable_land_per_farmer_related = Arable_land_per_farmerSerializer(many=True, read_only=True)
	crisisdb_gross_grain_shared_per_agricultural_population_related = Gross_grain_shared_per_agricultural_populationSerializer(many=True, read_only=True)
	crisisdb_net_grain_shared_per_agricultural_population_related = Net_grain_shared_per_agricultural_populationSerializer(many=True, read_only=True)
	crisisdb_surplus_related = SurplusSerializer(many=True, read_only=True)
	crisisdb_military_expense_related = Military_expenseSerializer(many=True, read_only=True)
	crisisdb_silver_inflow_related = Silver_inflowSerializer(many=True, read_only=True)
	crisisdb_silver_stock_related = Silver_stockSerializer(many=True, read_only=True)
	crisisdb_total_population_related = Total_populationSerializer(many=True, read_only=True)
	crisisdb_gdp_per_capita_related = Gdp_per_capitaSerializer(many=True, read_only=True)
	crisisdb_drought_event_related = Drought_eventSerializer(many=True, read_only=True)
	crisisdb_locust_event_related = Locust_eventSerializer(many=True, read_only=True)
	crisisdb_socioeconomic_turmoil_event_related = Socioeconomic_turmoil_eventSerializer(many=True, read_only=True)
	crisisdb_crop_failure_event_related = Crop_failure_eventSerializer(many=True, read_only=True)
	crisisdb_famine_event_related = Famine_eventSerializer(many=True, read_only=True)
	crisisdb_disease_outbreak_related = Disease_outbreakSerializer(many=True, read_only=True)

	class Meta:
		model = Polity
		fields = ['id', 'name', 'start_year', 'end_year', 'crisisdb_human_sacrifice_related', 'crisisdb_external_conflict_related', 'crisisdb_internal_conflict_related', 'crisisdb_external_conflict_side_related', 'crisisdb_agricultural_population_related', 'crisisdb_arable_land_related', 'crisisdb_arable_land_per_farmer_related', 'crisisdb_gross_grain_shared_per_agricultural_population_related', 'crisisdb_net_grain_shared_per_agricultural_population_related', 'crisisdb_surplus_related', 'crisisdb_military_expense_related', 'crisisdb_silver_inflow_related', 'crisisdb_silver_stock_related', 'crisisdb_total_population_related', 'crisisdb_gdp_per_capita_related', 'crisisdb_drought_event_related', 'crisisdb_locust_event_related', 'crisisdb_socioeconomic_turmoil_event_related', 'crisisdb_crop_failure_event_related', 'crisisdb_famine_event_related', 'crisisdb_disease_outbreak_related']
    
################ End of Serializers Imports
