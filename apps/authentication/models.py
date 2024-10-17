# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Add any custom fields you need
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # Add more fields as needed
