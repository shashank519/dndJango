# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Team, Level, Product, Channel, Payperiod, Component
# Register your models here.

admin.site.register(Team)
admin.site.register(Level)
admin.site.register(Product)
admin.site.register(Channel)
admin.site.register(Payperiod)
admin.site.register(Component)