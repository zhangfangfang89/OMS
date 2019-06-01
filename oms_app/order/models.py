# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid


class Order(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    order_no = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    create_by = models.CharField(max_length=64)

    def __str__(self):
        return self.order_no


class Product(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    classic = models.CharField(max_length=32)
    name = models.CharField(max_length=512)
    sku = models.CharField(max_length=32)
    price = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.order.order_no+":"+self.product.name


