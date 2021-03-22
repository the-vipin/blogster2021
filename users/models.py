from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class userProfile(models.Model):
    pfile = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to='userprofile_img/')
    Account = [
        ('r','reader'),
        ('w','writter'),
    ]
    Ac_type = models.CharField(max_length=100, choices = Account, blank=True, default='r')

    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.get_or_create(profile=instance)

