from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    SESHATADMIN = 1
    RA = 2
    SESHATEXPERT = 3
    PUBLICUSER = 4
    ROLE_CHOICES = (
        (SESHATADMIN, 'Seshat Admin'),
        (RA, 'Research Assistant'),
        (SESHATEXPERT, 'Seshat Expert'),
        (PUBLICUSER, 'Public User'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email_confirmed = models.BooleanField(default=False)
    location = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
