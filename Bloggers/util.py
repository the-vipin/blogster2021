import string
from django.utils.text import slugify
import random

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name+instance.registration_startdate)
    return slug