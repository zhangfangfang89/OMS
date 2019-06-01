# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from oms_app.user.models import *
from oms_app.order.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
