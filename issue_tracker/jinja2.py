from typing import Any

from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.defaultfilters import date, linebreaksbr
from django.urls import reverse
from django.utils import timezone
from jinja2 import Environment
from widget_tweaks.templatetags.widget_tweaks import add_class, append_attr


def datetimeformat(value, arg='DATETIME_FORMAT'):
    return date(timezone.localtime(value), arg)


def environment(**options: Any) -> Environment:
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'datetimeformat': datetimeformat,
        'add_class': add_class,
        'append_attr': append_attr,
        'linebreaksbr': linebreaksbr,

    })
    env.filters.update({
        'datetimeformat': datetimeformat,
        'add_class': add_class,
        'append_attr': append_attr,
        'linebreaksbr': linebreaksbr,

    })
    return env
