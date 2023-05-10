import re

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode


from django.utils.encoding import python_2_unicode_compatible

from .managers import EmailUserManager


@python_2_unicode_compatible

@python_2_unicode_compatible
class EmailUser(User):
    """
    class EmailUser(User):
    """
    objects = EmailUserManager()
    email = models.EmailField(_('email address'), unique=True)
    first_name = 'Vishal'

    def __str__(self):
        def __str__(self):
        return smart_unicode(self.email)

    def get_full_name(self):
        return smart_unicode(self.email)
    