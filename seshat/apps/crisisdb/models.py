
########## Beginning of Model Imports
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from datetime import date

import uuid

from django.utils import translation

from ..core.models import SeshatCommon, Certainty, Tags, Section, Subsection

########## End of Model Imports

########## Beginning of tuple choices for CrisisDB Models
SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES = (
('Peculiar Epidemics', 'Peculiar Epidemics'),
('Pestilence', 'Pestilence'),
('Miasm', 'Miasm'),
('Pox', 'Pox'),
('Uncertain Pestilence', 'Uncertain Pestilence'),
('Dysentery', 'Dysentery'),
('Malaria', 'Malaria'),
('Influenza', 'Influenza'),
('Cholera', 'Cholera'),
('Diptheria', 'Diptheria'),
('Plague', 'Plague'),
)

MAGNITUDE_DISEASE_OUTBREAK_CHOICES = (
('Uncertain', 'Uncertain'),
('Light', 'Light'),
('Heavy', 'Heavy'),
('No description', 'No description'),
('Heavy- Multiple Times', 'Heavy- Multiple Times'),
('No Happening', 'No Happening'),
('Moderate', 'Moderate'),
)

DURATION_DISEASE_OUTBREAK_CHOICES = (
('No description', 'No description'),
('Over 90 Days', 'Over 90 Days'),
('Uncertain', 'Uncertain'),
('30-60 Days', '30-60 Days'),
('1-10 Days', '1-10 Days'),
('60-90 Days', '60-90 Days'),
)


########## END of  tuple choices for CrisisDB Models

########## Beginning of Function Definitions for CrisisDB Models

def call_my_name(self):
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return self.name + " [for " + self.polity.name + " in " + str(self.year_from) + "]"
    else:
        return self.name + " [for " + self.polity.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"


def return_citations(self):
    return ', '.join(['<a href="' + citation.zoteroer() + '">' + citation.__str__() + ' </a>' for citation in self.citations.all()[:2]])


def clean_times(self):
    if (self.year_from and self.year_to) and self.year_from > self.year_to:
        raise ValidationError({
            'year_from': 'The start year is bigger than the end year!',
        })
    if self.year_from and (self.year_from < -10000 or self.year_from > date.today().year):
        raise ValidationError({
            'year_from': 'The start year is out of range!',
        })
    if self.year_from and (self.year_from < self.polity.start_year):
        raise ValidationError({
            'year_from': 'The start year is earlier than the start year of the corresponding polity!',
        })
    if self.year_to and (self.year_to > self.polity.end_year):
        raise ValidationError({
            'year_to': 'The end year is later than the end year of the corresponding polity!',
        })
    if self.year_to and (self.year_to < -10000 or self.year_to > date.today().year):
        raise ValidationError({
            'year_to': 'The end year is out of range!',
        })
    if not self.year_to and not self.year_from:
        raise ValidationError({
            'year_from': 'You need to enter at least one year (From or To)',
        })

########## End of Function Definitions for CrisisDB Models

########## Beginning of class Definitions for CrisisDB Models

class External_conflict(SeshatCommon):
    name = models.CharField(max_length=100, default="External_conflict")
    conflict_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict_name')
        verbose_name = 'External_conflict'
        verbose_name_plural = 'External_conflicts'

    @property
    def display_citations(self):
        return return_citations(self)


    def get_absolute_url(self):
        return reverse('internal_conflict-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.conflict_name
        
        
class Internal_conflict(SeshatCommon):
    name = models.CharField(max_length=100, default="Internal_conflict")
    conflict = models.CharField(max_length=500, blank=True, null=True)
    expenditure = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    leader = models.CharField(max_length=500, blank=True, null=True)
    casualty = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict', 'expenditure', 'leader', 'casualty')
        verbose_name = 'Internal_conflict'
        verbose_name_plural = 'Internal_conflicts'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('internal_conflict-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class External_conflict_side(SeshatCommon):
    name = models.CharField(max_length=100, default="External_conflict_side")
    conflict_id = models.ForeignKey(External_conflict, on_delete=models.SET_NULL, null=True, related_name="External_conflicts")
    expenditure = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    leader = models.CharField(max_length=500, blank=True, null=True)
    casualty = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict_id', 'expenditure', 'leader', 'casualty')
        verbose_name = 'External_conflict_side'
        verbose_name_plural = 'External_conflict_sides'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('external_conflict_side-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Agricultural_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Agricultural_population")
    agricultural_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'agricultural_population')
        verbose_name = 'Agricultural_population'
        verbose_name_plural = 'Agricultural_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('agricultural_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Arable_land(SeshatCommon):
    name = models.CharField(max_length=100, default="Arable_land")
    arable_land = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'arable_land')
        verbose_name = 'Arable_land'
        verbose_name_plural = 'Arable_lands'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('arable_land-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Arable_land_per_farmer(SeshatCommon):
    name = models.CharField(max_length=100, default="Arable_land_per_farmer")
    arable_land_per_farmer = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'arable_land_per_farmer')
        verbose_name = 'Arable_land_per_farmer'
        verbose_name_plural = 'Arable_land_per_farmers'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('arable_land_per_farmer-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gross_grain_shared_per_agricultural_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Gross_grain_shared_per_agricultural_population")
    gross_grain_shared_per_agricultural_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'gross_grain_shared_per_agricultural_population')
        verbose_name = 'Gross_grain_shared_per_agricultural_population'
        verbose_name_plural = 'Gross_grain_shared_per_agricultural_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('gross_grain_shared_per_agricultural_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Net_grain_shared_per_agricultural_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Net_grain_shared_per_agricultural_population")
    net_grain_shared_per_agricultural_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'net_grain_shared_per_agricultural_population')
        verbose_name = 'Net_grain_shared_per_agricultural_population'
        verbose_name_plural = 'Net_grain_shared_per_agricultural_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('net_grain_shared_per_agricultural_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Surplus(SeshatCommon):
    name = models.CharField(max_length=100, default="Surplus")
    surplus = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'surplus')
        verbose_name = 'Surplus'
        verbose_name_plural = 'Surplus'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('surplus-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Military_expense(SeshatCommon):
    name = models.CharField(max_length=100, default="Military_expense")
    conflict = models.CharField(max_length=500, blank=True, null=True)
    expenditure = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'conflict', 'expenditure')
        verbose_name = 'Military_expense'
        verbose_name_plural = 'Military_expenses'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('military_expense-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Silver_inflow(SeshatCommon):
    name = models.CharField(max_length=100, default="Silver_inflow")
    silver_inflow = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'silver_inflow')
        verbose_name = 'Silver_inflow'
        verbose_name_plural = 'Silver_inflows'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('silver_inflow-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Silver_stock(SeshatCommon):
    name = models.CharField(max_length=100, default="Silver_stock")
    silver_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'silver_stock')
        verbose_name = 'Silver_stock'
        verbose_name_plural = 'Silver_stocks'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('silver_stock-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Total_population(SeshatCommon):
    name = models.CharField(max_length=100, default="Total_population")
    total_population = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'total_population')
        verbose_name = 'Total_population'
        verbose_name_plural = 'Total_populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('total_population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gdp_per_capita(SeshatCommon):
    name = models.CharField(max_length=100, default="Gdp_per_capita")
    gdp_per_capita = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'gdp_per_capita')
        verbose_name = 'Gdp_per_capita'
        verbose_name_plural = 'Gdp_per_capitas'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('gdp_per_capita-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Drought_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Drought_event")
    drought_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'drought_event')
        verbose_name = 'Drought_event'
        verbose_name_plural = 'Drought_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('drought_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Locust_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Locust_event")
    locust_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'locust_event')
        verbose_name = 'Locust_event'
        verbose_name_plural = 'Locust_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('locust_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Socioeconomic_turmoil_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Socioeconomic_turmoil_event")
    socioeconomic_turmoil_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'socioeconomic_turmoil_event')
        verbose_name = 'Socioeconomic_turmoil_event'
        verbose_name_plural = 'Socioeconomic_turmoil_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('socioeconomic_turmoil_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Crop_failure_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Crop_failure_event")
    crop_failure_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'crop_failure_event')
        verbose_name = 'Crop_failure_event'
        verbose_name_plural = 'Crop_failure_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('crop_failure_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Famine_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Famine_event")
    famine_event = models.IntegerField(blank=True, null=True)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'famine_event')
        verbose_name = 'Famine_event'
        verbose_name_plural = 'Famine_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('famine_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Disease_outbreak(SeshatCommon):
    name = models.CharField(max_length=100, default="Disease_outbreak")
    longitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    elevation = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    sub_category = models.CharField(max_length=500, choices=SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES)
    magnitude = models.CharField(max_length=500, choices=MAGNITUDE_DISEASE_OUTBREAK_CHOICES)
    duration = models.CharField(max_length=500, choices=DURATION_DISEASE_OUTBREAK_CHOICES)

    class Meta:
        # unique_together = ('polity', 'year_from', 'year_to', 'tag', 'longitude', 'latitude', 'elevation', 'sub_category', 'magnitude', 'duration')
        verbose_name = 'Disease_outbreak'
        verbose_name_plural = 'Disease_outbreaks'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('disease_outbreak-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
########## END of class Definitions for CrisisDB Models
