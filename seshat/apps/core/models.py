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

from seshat.apps.accounts.models import Seshat_Expert


from django.utils import translation
from django.contrib import messages
from django.core.validators import URLValidator


# APS = 'A;P*'
# AP = 'A;P'
# NFY = 'NFY'
# UU = 'U*'
# AA = 'A'
# PP = 'P'
# PS = 'P*'
# AS = 'A*'
# Certainty = (
#     (APS, 'Absent Present Suspected'),
#     (AP, 'Absent Present'),
#     (UU, 'Unknown'),
#     (AA, 'Absent'),
#     (PP, 'Present'),
#     (AS, 'Absent Suspected'),
#     (PS, 'Present Suspected'),
#     (NFY, 'Not Filled Yet'),
# )

# Tags = (
#     ('TRS', 'Evidenced'),
#     ('DSP', 'Disputed'),
#     ('SSP', 'Suspected'),
#     ('IFR', 'Inferred'),
#     ('UNK', 'Unknown'),
# )



Tags = (
    ('TRS', 'Evidenced'),
    ('SSP', 'Suspected'),
    ('IFR', 'Inferred'),
)

APS = 'A;P*'
AP = 'A;P'
NFY = 'NFY'
UU = 'U*'
AA = 'A'
U = "U"
PP = 'P'
PS = 'P*'
AS = 'A*'
P_TO_A = "P~A" 
A_TO_P = "A~P" 


WORLD_REGION_CHOICES = (('Europe', 'Europe'),
        ('Southwest Asia', 'Southwest Asia'),
        ('Africa', 'Africa'),
        ('Central Eurasia', 'Central Eurasia'),
        ('South Asia', 'South Asia'),
        ('Southeast Asia', 'Southeast Asia'),
        ('East Asia', 'East Asia'),
        ('Oceania-Australia', 'Oceania-Australia'),
        ('North America', 'North America'),
        ('South America', 'South America'))

Certainty = (
    (AP, 'scholarly disagreement or uncertainty'),
    (UU, 'Suspected Unknown'),
    (AA, 'Absent'),
    (PP, 'Present'),
    (AS, 'Inferred Absent'),
    (PS, 'Inferred Present'),
    (NFY, 'not applicable; no other code is appropriate'),
    (U, 'Unknown'),
    (P_TO_A, 'uncertainty about when a given trait disappears'),
    (A_TO_P, 'uncertainty about when a given trait appears'),
)

def return_citations_for_comments(self):
    if self.comment_citations.all():
        return ', '.join(['<a href="' + citation.zoteroer() + '">' + citation.citation_short_title + ' </a>' for citation in self.comment_citations.all()[:2]])


class Nga(models.Model):
    name = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.DecimalField(max_digits= 16, decimal_places = 12, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 16, decimal_places = 12, blank=True, null=True)
    capital_city =  models.CharField(max_length=100, blank=True, null=True)
    nga_code = models.CharField(max_length=20, blank=True, null=True)
    fao_country = models.CharField(max_length=100, blank=True, null=True)
    world_region = models.CharField(max_length=100, choices=WORLD_REGION_CHOICES, default="Europe")

    def get_absolute_url(self):
        return reverse('ngas')

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name




class Polity(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    long_name = models.CharField(max_length=200, blank=True, null=True)
    new_name = models.CharField(max_length=100, blank=True, null=True)
    home_nga = models.ForeignKey(Nga, on_delete=models.SET_NULL, null=True, blank=True, related_name="home_nga")

    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'polity'
        verbose_name_plural = 'polities'

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        if self.long_name and self.new_name:
            return f"{self.long_name} ({self.new_name})"
        else:
            return self.name

    class Meta:
        unique_together = ("name",)
        ordering = ['long_name']

class Capital(models.Model):
    name = models.CharField(max_length=100)
    current_country = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 11, decimal_places = 8, blank=True, null=True)
    longitude = models.DecimalField(max_digits= 11, decimal_places = 8, blank=True, null=True)
    polity_cap = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True, related_name="polity_caps")  
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,) 
    url_on_the_map =  models.URLField(max_length=200, blank=True, null=True)
    is_verified = models.BooleanField(default=False, blank=True, null=True)

    note = models.TextField(
        blank=True, null=True,)

    def get_absolute_url(self):
        return reverse('capitals')

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        return self.name
    class Meta:
       #ordering = ['-year']
       ordering = ['is_verified']

    
class Ngapolityrel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    polity_party = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True, related_name="polity_sides")
    nga_party = models.ForeignKey(Nga, on_delete=models.SET_NULL, null=True, related_name="nga_sides")
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,) 
    is_home_nga = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        if self.name:
            return self.name
        elif self.polity_party and self.nga_party:
            return f"{self.polity_party.name}'s settlement in {self.nga_party.name}"
        else:
            return str(self.id)

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
    title = models.CharField(max_length=500,)
    year = models.IntegerField(blank=True, null=True, )
    creator = models.CharField(max_length=500, )
    zotero_link = models.CharField(max_length=500, blank=True, null=True)
    long_name = models.CharField(max_length=500, blank=True, null=True)
    url_link = models.TextField(max_length=500, validators=[URLValidator()], blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        """string for epresenting the model obj in Admin Site"""
        original_title = self.title
        if len(original_title) > 50:
            shorter_title = original_title[0:50] + original_title[50:].split(" ")[0] + "..."
        else:
            shorter_title = original_title
        return "(%s_%s): %s _ %s" % (self.creator, self.year, shorter_title, self.id)

    @property
    def reference_short_title(self):
        """Second String for representing the Model Object"""

        original_long_name = self.long_name
        if original_long_name and len(original_long_name) > 40:
           shorter_name = original_long_name[0:40] + original_long_name[40:].split(" ")[0] + "..."
        elif original_long_name:
           shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"

        if self.zotero_link and "NOZOTERO_LINK" in self.zotero_link:
            return f'(NOZOTERO_REF: {shorter_name})'
        elif self.title:
            return self.title
        else:
            return "NO_TITLES_PROVIDED"

    def get_absolute_url(self):
        return reverse('references')

    class Meta:
       #ordering = ['-year']
       unique_together = ("zotero_link",)
       ordering = ['-created_date', 'title']



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
        if self.ref.zotero_link and "NOZOTERO_LINK" not in self.ref.zotero_link:
            my_zotero_link = "https://www.zotero.org/groups/1051264/seshat_databank/items/" + \
                str(self.ref.zotero_link)
        else:
            my_zotero_link = reverse('citation-update', args=[str(self.id)])
        return my_zotero_link

    # def page_from_maker(self):
    #     return(str(self.page_from))
    # def page_to_maker(self):
    #     return(str(self.page_to))

    def __str__(self) -> str:
        """String for representing the Model Object"""
        if self.ref and self.ref.title:
            original_title = self.ref.title
        else:
            original_title = "REFERENCE_WITH_NO_TITLE"
        if original_title and len(original_title) > 50:
            shorter_title = original_title[0:50] + original_title[50:].split(" ")[0] + "..."
        elif original_title:
            shorter_title = original_title
        else:
            shorter_title = "BlaBlaBla"

        if self.ref and self.ref.long_name:
            original_long_name = self.ref.long_name
        else:
            original_long_name = "REFERENCE_WITH_NO_LONG_NAME"
        if original_long_name and len(original_long_name) > 50:
           shorter_name = original_long_name[0:50] + original_long_name[50:].split(" ")[0] + "..."
        elif original_long_name:
           shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"
        
        if self.ref and self.ref.zotero_link and "NOZOTERO_LINK" in self.ref.zotero_link:
            return f'(NOZOTERO: {shorter_name})'
        if self.ref and self.ref.creator:
            if self.page_from == None and self.page_to == None:
                return '({0} {1}): {2}'.format(self.ref.creator, self.ref.year, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
                return '({0} {1}, p. {2}): {3}'.format(self.ref.creator, self.ref.year, self.page_from, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
                return '({0} {1}, p. {2}): {3}'.format(self.ref.creator, self.ref.year, self.page_to, shorter_title)
            elif self.page_from and self.page_to:
                return '({0} {1}, pp. {2}-{3}): {4}'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to, shorter_title)
            else:
                return '({0} {1}): {2}'.format(self.ref.creator, self.ref.year, shorter_title)
        else:
            print("BADREF::::")
            print(self.id)
            print(self.modified_date)

            
            return "BADBADREFERENCE"
        
    def full_citation_display(self) -> str:
        """String for representing the Model Object"""
        if self.ref and self.ref.title:
            original_title = self.ref.title
        else:
            original_title = "REFERENCE_WITH_NO_TITLE"
        if original_title:
            shorter_title = original_title
        else:
            shorter_title = "BlaBlaBla"

        if self.ref and self.ref.long_name:
            original_long_name = self.ref.long_name
        else:
            original_long_name = "REFERENCE_WITH_NO_LONG_NAME"
        if original_long_name:
           shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"
        
        if self.ref and self.ref.zotero_link and "NOZOTERO_LINK" in self.ref.zotero_link:
            return f'(NOZOTERO: {shorter_name})'
        if self.ref and self.ref.creator:
            if self.page_from == None and self.page_to == None:
                return '<b class="fw-bold">({0} {1})</b>: {2}'.format(self.ref.creator, self.ref.year, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
                return '<b class="fw-bold">({0} {1}, p. {2})</b>: {3}'.format(self.ref.creator, self.ref.year, self.page_from, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
                return '<b class="fw-bold">({0} {1}, p. {2})</b>: {3}'.format(self.ref.creator, self.ref.year, self.page_to, shorter_title)
            elif self.page_from and self.page_to:
                return '<b class="fw-bold">({0} {1}, pp. {2}-{3})</b>: {4}'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to, shorter_title)
            else:
                return '<b class="fw-bold">({0} {1})</b>: {2}'.format(self.ref.creator, self.ref.year, shorter_title)
        else:
            print("BADREF::::")
            print(self.id)
            print(self.modified_date)

            
            return "BADBADREFERENCE"
    
    class Meta:
       #ordering = ['-year']
       ordering = ['-modified_date']
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
    
    @property
    def citation_short_title(self):
        """Second String for representing the Model Object"""

        original_long_name = self.ref.long_name
        if original_long_name and len(original_long_name) > 40:
           shorter_name = original_long_name[0:40] + original_long_name[40:].split(" ")[0] + "..."
        elif original_long_name:
           shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"

        if "NOZOTERO_LINK" in self.ref.zotero_link:
            return f'(NOZOTERO: {shorter_name})'

        if self.page_from == None and self.page_to == None:
            return '[{0} {1}]'.format(self.ref.creator, self.ref.year)
        elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
            return '[{0} {1}, p. {2}]'.format(self.ref.creator, self.ref.year, self.page_from)
        elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
            return '[{0} {1}, p. {2}]'.format(self.ref.creator, self.ref.year, self.page_to)
        elif self.page_from and self.page_to:
            return '[{0} {1}, pp. {2}-{3}]'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to)
        else:
            return '[{0} {1}]'.format(self.ref.creator, self.ref.year)
    
    def get_absolute_url(self):
        return reverse('citations')
    
    def save(self, *args, **kwargs):
        try:
            super(Citation, self).save(*args, **kwargs)
        except IntegrityError as e:
            print(e)

class SeshatComment(models.Model):
    text = models.TextField(blank=True, null=True,)

    def zoteroer(self):
        if self.ref.zotero_link and "NOZOTERO_LINK" not in self.ref.zotero_link:
            my_zotero_link = "https://www.zotero.org/groups/1051264/seshat_databank/items/" + \
                str(self.ref.zotero_link)
        else:
            my_zotero_link = "#"
        return my_zotero_link

    def __str__(self) -> str:
        all_comment_parts = self.inner_comments_related.all().order_by('comment_order')

        if all_comment_parts:
            comment_parts = []
            for comment_part in all_comment_parts:
                if comment_part.citation_index:
                    separation_point = comment_part.citation_index
                    comment_full_text = comment_part.comment_part_text[0:separation_point] + str(comment_part.display_citations) + " " + comment_part.comment_part_text[separation_point:]
                else:
                    if comment_part.comment_part_text and comment_part.comment_part_text.startswith("<br>"):
                        if comment_part.display_citations:
                            comment_full_text = comment_part.comment_part_text[4:] + str(comment_part.display_citations)
                        else:
                            comment_full_text = comment_part.comment_part_text[4:]
                    else:
                        if comment_part.display_citations:
                            comment_full_text = comment_part.comment_part_text + str(comment_part.display_citations)
                        else:
                            comment_full_text = comment_part.comment_part_text

                comment_parts.append(comment_full_text)
            #comment_parts = ["<b>" + str(comment_part.comment_curator)+ "</b>: " + str(comment_part.comment_part_text) + str(comment_part.display_citations) for comment_part in all_comment_parts]
            #ref_parts = ['<a href="#">' + str(comment_part.comment_order) + ' </a>' for comment_part in all_comment_parts]
            if not comment_parts or comment_parts == [None]:
                to_be_shown = " Nothing "
            else:
                to_be_shown = " ".join(comment_parts)
                
        elif self.text and not all_comment_parts:
            to_be_shown = "No descriptions."
        else:
            to_be_shown = "EMPTY_COMMENT"
        return f'{to_be_shown}'
    
    def get_absolute_url(self):
        return reverse('seshatcomments')



class SeshatCommentPart(models.Model):
    comment = models.ForeignKey(SeshatComment, on_delete=models.SET_NULL, related_name="inner_comments_related",
                               related_query_name="inner_comments_related", null=True, blank=True)
    comment_part_text = models.TextField(blank=True, null=True,)
    comment_curator = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    comment_order = models.IntegerField(blank=True, null=True,)
    comment_citations = ManyToManyField(
        Citation, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    citation_index = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    
    @property
    def display_citations(self):
        return return_citations_for_comments(self)

    def get_absolute_url(self):
        return reverse('seshatcomment-update',  args=[str(self.comment.id)])

    class Meta:
        ordering = ['comment_order', "modified_date"]

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
    is_disputed = models.BooleanField(default=False, blank=True, null=True)
    is_uncertain = models.BooleanField(default=False, blank=True, null=True)
    expert_reviewed = models.BooleanField(null=True, blank=True, default=True)
    drb_reviewed = models.BooleanField(null=True, blank=True, default=False)
    curator = models.ManyToManyField(Seshat_Expert,  related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    comment = models.ForeignKey(SeshatComment, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    class Meta:
        abstract = True
        ordering = ['polity']


# class Annual_wages(SeshatCommon):
#     name = models.CharField(max_length=100, default="Annual_wages")
#     annual_wages = models.IntegerField(blank=True, null=True)
#     job_category = models.CharField(choices=job_category_annual_wages_choices)
#     job_description = models.CharField(
#         choices=job_description_annual_wages_choices)


