from __future__ import unicode_literals
import re
import warnings
import string
from django.utils.text import slugify
import random


def random_digita_generator(size =10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))