from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date

import uuid

from django.utils import translation


APS = 'A;P*'
AP = 'A;P'
NFY = 'NFY'
UU = 'U*'
AA = 'A'
PP = 'P'
PS = 'P*'
AS = 'A*'
Certainty = (
    (APS, 'Absent Present Suspected'),
    (AP, 'Absent Present'),
    (UU, 'Unknown'),
    (AA, 'Absent'),
    (PP, 'Present'),
    (AS, 'Absent Suspected'),
    (PS, 'Present Suspected'),
    (NFY, 'Not Filled Yet'),
)

Tags = (
    ('TRS', 'Evidenced'),
    ('DSP', 'Disputed'),
    ('SSP', 'Suspected'),
    ('IFR', 'Inferred'),
    ('UNK', 'Unknown'),
)


class Polity(models.Model):
    name = models.CharField(max_length=100)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'polity'
        verbose_name_plural = 'polities'

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)
    polity = models.ForeignKey(
        Polity, on_delete=models.SET_NULL, null=True, related_name="countries")

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


class Subsection(models.Model):
    name = models.CharField(max_length=200)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, related_name="subsections")

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name


# def get_all_vars_for_hierarchy():
#     my_vars = []
#     for ct in ContentType.objects.all():
#         m = ct.model_class()
#         if m.__module__ == "seshat.apps.crisisdb.models":
#             app_name = m.__module__.split('.')[-2] + '_'
#             better_key = app_name + m.__name__
#             better_value = m.__name__.replace('_', ' ')
#             inner_tuple = (better_key, better_value)
#             my_vars.append(inner_tuple)
#             #print(better_key, ': ', better_value)
#             # print(f"{m.__module__}.{m.__name__}\t{m._default_manager.count()}")
#     return (my_vars)


# def ready(self):
#     def get_all_vars_for_hierarchy():
#         my_vars = []
#         for ct in ContentType.objects.all():
#             m = ct.model_class()
#             if m.__module__ == "seshat.apps.crisisdb.models":
#                 app_name = m.__module__.split('.')[-2] + '_'
#                 better_key = app_name + m.__name__
#                 better_value = m.__name__.replace('_', ' ')
#                 inner_tuple = (better_key, better_value)
#                 my_vars.append(inner_tuple)
#                 #print(better_key, ': ', better_value)
#                 # print(f"{m.__module__}.{m.__name__}\t{m._default_manager.count()}")
#         return (my_vars)
#     print(get_all_vars_for_hierarchy())


class VariableHierarchy(models.Model):
    name = models.CharField(
        max_length=200)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, blank=True,)
    subsection = models.ForeignKey(
        Subsection, on_delete=models.SET_NULL, null=True, blank=True,)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name

    class Meta:
        unique_together = ("name", "section", "subsection")


class Reference(models.Model):
    """Model Representing a Reference"""
    title = models.CharField(
        max_length=200, help_text='Enter a title')
    year = models.IntegerField(
        blank=True, null=True, help_text="year of Publication")
    creator = models.CharField(
        max_length=100, help_text="Creator of pub")
    zotero_link = models.CharField(
        max_length=100, help_text="choose the 8-digit Zotero link")
    long_name = models.CharField(
        max_length=500, help_text='Enter the long name', blank=True, null=True)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return "(%s_%s)" % (self.creator, self.year)


class Citation(models.Model):
    """Model representing a specific citation."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique Id for this particular citation")
    ref = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True, related_name="citation")
    page_from = models.IntegerField(null=True, blank=True)
    page_to = models.IntegerField(null=True, blank=True)

    # class Meta:
    #     permissions = (("can_mark_returned", "Set book as returned"),
    #                    ("can_renew", "Can Renew A Book"),)

    def zoteroer(self):
        if self.ref.zotero_link:
            my_zotero_link = "https://www.zotero.org/groups/1051264/seshat_databank/items/" + \
                str(self.ref.zotero_link)
        else:
            my_zotero_link = "#"
        return my_zotero_link

    def __str__(self) -> str:
        """String for representing the Model Object"""
        if self.page_from == self.page_to or ((not self.page_to) and self.page_from):
            return '({0}_{1}, p. {2})'.format(self.ref.creator, self.ref.year, self.page_from)
        elif self.page_from and self.page_to:
            return '({0}_{1}, pp. {2}-{3})'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to)
        else:
            return '({0}_{1})'.format(self.ref.creator, self.ref.year)


class SeshatCommon(models.Model):
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss", blank=True, null=True,)
    subsection = models.ForeignKey(
        Subsection, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss", blank=True, null=True,)
    name = models.CharField(
        max_length=200,)
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True)
    # exra vars will be added in between
    description = models.TextField(
        blank=True, null=True, help_text="Add an Optional description or a personal comment above.")
    note = models.TextField(
        blank=True, null=True, help_text="Add an Optional note or a personal comment above.")
    citations = ManyToManyField(
        Citation, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", help_text=mark_safe('Select one or more references for this fact. Hold CTRL to select multiple.'), blank=True,)
    finalized = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    tag = models.CharField(max_length=5, choices=Tags, default="TRS")

    class Meta:
        abstract = True
        ordering = ['polity']


# class Annual_wages(SeshatCommon):
#     name = models.CharField(max_length=100, default="Annual_wages")
#     annual_wages = models.IntegerField(blank=True, null=True)
#     job_category = models.CharField(choices=job_category_annual_wages_choices)
#     job_description = models.CharField(
#         choices=job_description_annual_wages_choices)
