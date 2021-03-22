from __future__ import unicode_literals
import re
import warnings
import string
from django.utils.text import slugify
import random


def random_string_generator(size =10, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
def random_digita_generator(size =10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.BloggerName)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_string_generator(size =4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_for_blogPost(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else: 
        #slug = slugify(instance.Blogtiltle+'-by-'+instance.BloggerAc.BloggerName)
        rndmstr = random_digita_generator(size=6)
        slug = slugify(instance.Blogtiltle+'-'+rndmstr)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_digita_generator(size =6)
        )
        return unique_slug_generator_for_blogPost(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_for_askquestion(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else: 
        #slug = slugify(instance.Blogtiltle+'-by-'+instance.BloggerAc.BloggerName)
        rndmstr = random_string_generator(size=10)
        slug = slugify(rndmstr)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_string_generator(size =10)
        )
        return unique_slug_generator_for_askquestion(instance, new_slug=new_slug)
    return slug
    

IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


def get_ip(request):
    """
    Retrieves the remote IP address from the request data.  If the user is
    behind a proxy, they may have a comma-separated list of IP addresses, so
    we need to account for that.  In such a case, only the first IP in the
    list will be retrieved.  Also, some hosts that use a proxy will put the
    REMOTE_ADDR into HTTP_X_FORWARDED_FOR.  This will handle pulling back the
    IP from the proper place.

    **NOTE** This function was taken from django-tracking (MIT LICENSE)
             http://code.google.com/p/django-tracking/
    """

    # if neither header contain a value, just use local loopback
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR',
                                  request.META.get('REMOTE_ADDR', '127.0.0.1'))
    if ip_address:
        # make sure we have one and only one IP
        try:
            ip_address = IP_RE.match(ip_address)
            if ip_address:
                ip_address = ip_address.group(0)
            else:
                # no IP, probably from some dirty proxy or other device
                # throw in some bogus IP
                ip_address = '10.0.0.1'
        except IndexError:
            pass

    return ip_address

