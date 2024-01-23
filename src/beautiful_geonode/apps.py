# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
import os
from django.apps import AppConfig as BaseAppConfig
from django.db import models
from django import forms

try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import ugettext_lazy as _

def run_setup_hooks(*args, **kwargs):
    from django.conf import settings
    from .celeryapp import app as celeryapp

    LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
    settings.TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))

    if celeryapp not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (celeryapp,)

class AppConfig(BaseAppConfig):
    name = "beautiful_geonode"
    label = "beautiful_geonode"

    def _get_logger(self):
        import logging
        return logging.getLogger(self.__class__.__module__)

    def patch_dataset(self, cls):
        self._get_logger().info("Patching Dataset")
        is_tabular = models.BooleanField(_("Is tabular?"), default=False)
        cls.add_to_class('is_tabular', is_tabular)

    def patch_dataset_form(self, cls):
        self._get_logger().info("Patching Dataset form")
        is_tabular = forms.BooleanField(label=_("Is tabular?"), required=False)
        cls.base_fields['is_tabular'] = is_tabular

    def patch_dataset_save(self, sender, instance, created, **kwargs):
        self._get_logger().info("Patching Dataset save")
        if instance.is_tabular:
            type(instance).objects.filter(pk=instance.pk).update(subtype='tabular')
       
    def ready(self):
        super(AppConfig, self).ready()
        run_setup_hooks()

        try:
            from geonode.layers.models import Dataset
            from geonode.layers.forms import DatasetForm
            #self.patch_dataset(Dataset)
            #self.patch_dataset_form(DatasetForm)
            #models.signals.post_save.connect(self.patch_dataset_save, sender=Dataset)
        except Exception as e:
            self._get_logger().error("Error patching Dataset: %s" % e)