# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# modelos ---------------------------
class temperatura(models.Model):
    fecha = models.DateTimeField(default=datetime.now, blank=False, null=False)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "temperaturas"

    def __unicode__(self):
            return str(self.fecha)
