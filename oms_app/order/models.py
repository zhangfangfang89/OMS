# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class product(models.Model):
    product_classification = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

