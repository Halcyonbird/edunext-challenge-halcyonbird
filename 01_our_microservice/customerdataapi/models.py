# -*- coding: utf-8 -*-
"""
Database models for customerdataapi.
"""

from __future__ import absolute_import, unicode_literals

import collections
import uuid
import jsonfield

from django.db import models


class CustomerData(models.Model):
    """
    A simple model to store our customer data
    """
    ## I re-design the model with validation parameters ##
    ## Add the DOWNGRADE_DATE UPGRADE_DATE fields ##
    ## all data can be null and blank to maintain data flexibility  ##
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name   
    SUBSCRIPTION = models.CharField(max_length=7, choices=[('free', 'Free'),('basic', 'Basic'),('premium', 'Premium')], default='1', null=True)
    CREATION_DATE = models.DateTimeField(auto_now_add=True, blank=True ,null=True)
    LAST_PAYMENT_DATE = models.DateTimeField(auto_now=False, blank=True ,null=True)
    DOWNGRADE_DATE = models.DateTimeField(auto_now=False, blank=True ,null=True)
    UPGRADE_DATE = models.DateTimeField(auto_now=False, blank=True ,null=True)
    theme_name = models.CharField(max_length=40, blank=True, null=True)
    ENABLED_FEATURES = jsonfield.JSONField(blank=True, null=True, load_kwargs={'object_pairs_hook': collections.OrderedDict})
    language_code = models.CharField(max_length=25, blank=True ,null=True, default="en")
    banner_message = models.CharField(max_length=150, blank=True ,null=True)
    displayed_timezone = models.CharField(max_length=200, blank=True, null=True)
    user_profile_image = models.URLField(blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "CustomerData with id <{}>".format(self.id)
    

