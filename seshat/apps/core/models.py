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
from django.db.models import Q
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

import uuid

from django.utils import translation
from django.contrib import messages
from django.core.validators import URLValidator


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
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'polity'
        verbose_name_plural = 'polities'

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name

    class Meta:
        unique_together = ("name",)
    


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
    
    class Meta:
        unique_together = ("name",)


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name

    class Meta:
        unique_together = ("name",)


class Subsection(models.Model):
    name = models.CharField(max_length=200)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, related_name="subsections")

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name
    
    class Meta:
        unique_together = ("name", "section")


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


class Variablehierarchy(models.Model):
    name = models.CharField(
        max_length=200)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, blank=True,)
    subsection = models.ForeignKey(
        Subsection, on_delete=models.SET_NULL, null=True, blank=True,)
    is_verified = models.BooleanField(default=False)
    explanation = models.TextField(blank=True, null=True,)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name

    class Meta:
        unique_together = ("name", "section", "subsection")


class Reference(models.Model):
    """Model Representing a Reference"""
    title = models.CharField(
        max_length=500, help_text='Enter a title')
    year = models.IntegerField(
        blank=True, null=True, help_text="year of Publication")
    creator = models.CharField(
        max_length=500, help_text="Creator of pub")
    zotero_link = models.CharField(
        max_length=500, help_text="choose the 8-digit Zotero link", blank=True, null=True)
    long_name = models.CharField(
        max_length=500, help_text='Enter the long name', blank=True, null=True)
    url_link = models.TextField(max_length=500, validators=[URLValidator()], blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        original_title = self.title
        if len(original_title) > 50:
            shorter_title = original_title[0:50] + original_title[50:].split(" ")[0] + "..."
        else:
            shorter_title = original_title
        return "(%s_%s): %s" % (self.creator, self.year, shorter_title)

    class Meta:
       #ordering = ['-year']
       unique_together = ("title", "zotero_link")
       ordering = ['-modified_date']



class Citation(models.Model):
    """Model representing a specific citation."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique Id for this particular citation")
    ref = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True, related_name="citation")
    page_from = models.IntegerField(null=True, blank=True)
    page_to = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

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

    # def page_from_maker(self):
    #     return(str(self.page_from))
    # def page_to_maker(self):
    #     return(str(self.page_to))

    def __str__(self) -> str:
        """String for representing the Model Object"""
        original_title = self.ref.title
        if len(original_title) > 50:
            shorter_title = original_title[0:50] + original_title[50:].split(" ")[0] + "..."
        else:
            shorter_title = original_title
        
        if self.page_from == None and self.page_to == None:
            return '({0}_{1}): {2}'.format(self.ref.creator, self.ref.year, shorter_title)
        elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
            return '({0}_{1}, p. {2}): {3}'.format(self.ref.creator, self.ref.year, self.page_from, shorter_title)
        elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
            return '({0}_{1}, p. {2}): {3}'.format(self.ref.creator, self.ref.year, self.page_to, shorter_title)
        elif self.page_from and self.page_to:
            return '({0}_{1}, pp. {2}-{3}): {4}'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to, shorter_title)
        else:
            return '({0}_{1}): {2}'.format(self.ref.creator, self.ref.year, shorter_title)
    class Meta:
       #ordering = ['-year']
       ordering = ['-created_date']
       constraints = [
        models.UniqueConstraint(
            name="No_PAGE_TO_AND_FROM",
            fields=("ref",),
            condition=(Q(page_to__isnull=True) & Q(page_from__isnull=True)) 
        ),
        models.UniqueConstraint(
            name="No_PAGE_TO",
            fields=("ref", "page_from"),
            condition=Q(page_to__isnull=True)
        ),
        models.UniqueConstraint(
            name="No_PAGE_FROM",
            fields=("ref", "page_to"),
            condition=Q(page_from__isnull=True)
        ),
       ]
       #unique_together = ["ref", "page_from", "page_to"]
    def get_absolute_url(self):
        return reverse('citations')
    
    def save(self, *args, **kwargs):
        try:
            super(Citation, self).save(*args, **kwargs)
        except IntegrityError as e:
            print(e)

class SeshatCommon(models.Model):
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    name = models.CharField(
        max_length=200,)
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,)
    # exra vars will be added in between
    description = models.TextField(
        blank=True, null=True,)
    note = models.TextField(
        blank=True, null=True,)
    citations = ManyToManyField(
        Citation, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
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


