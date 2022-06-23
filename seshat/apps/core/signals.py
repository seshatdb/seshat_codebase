from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Reference, Citation

@receiver(post_save, sender=Reference)
def create_citation(sender, instance, created, **kwargs):
    if created:
        Citation.objects.create(ref=instance)

# @receiver(post_save, sender=Reference)
# def save_citation(sender, instance, **kwargs):
#     instance.citation.save()