# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=64, unique=True, name='user_name')
    password = models.CharField(max_length=64, name='password')
    create_date = models.DateTimeField(auto_now=True)
    create_by = models.CharField(max_length=64)
    email = models.EmailField()
    last_login = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=64)
    update_password_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name
