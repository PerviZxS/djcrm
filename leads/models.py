from random import choice
from tokenize import blank_re

from django.db import models

class Lead(models.Model):

    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Instagram', 'Instagram'),
        ('X', 'X'),
        ('Google', 'Google'),
    )


    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)

    phone = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length= 100)


    profile_picture = models.ImaageField(blank = True, null = True)
    special_file = models.FileField(blank = True, null = True)


