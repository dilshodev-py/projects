from __future__ import unicode_literals

import datetime

from rangefilter.filters import DateRangeFilter

try:
    import pytz
except ImportError:
    pytz = None

try:
    import csp
except ImportError:
    csp = None

from collections import OrderedDict

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _


class CustomDateField(forms.DateField):

    def to_python(self, value):
        if value in self.empty_values:
            return None
        if isinstance(value, datetime.datetime):
            return value.date()
        if isinstance(value, datetime.date):
            return value
        if isinstance(value, list):
            value = value[0]
        return super().to_python(value)

    def bound_data(self, data, initial):
        b_data=super().bound_data(data, initial)
        return b_data[0]


class CustomDateRangeFilter(DateRangeFilter):

    def _get_form_fields(self):
        return OrderedDict(
            (
                (
                    self.lookup_kwarg_gte,
                    CustomDateField(
                        label="",
                        widget=AdminDateWidget(
                            attrs={"placeholder": "... dan"}
                        ),
                        localize=True,
                        required=False,
                        initial=self.default_gte,
                    ),
                ),
                (
                    self.lookup_kwarg_lte,
                    CustomDateField(
                        label="",
                        widget=AdminDateWidget(
                            attrs={"placeholder": "... gacha"}
                        ),
                        localize=True,
                        required=False,
                        initial=self.default_lte,
                    ),
                ),
            )
        )
