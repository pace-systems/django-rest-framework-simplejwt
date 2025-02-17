from calendar import timegm
from datetime import datetime, timezone

from django.conf import settings
from django.utils.functional import lazy
from django.utils.timezone import is_naive, make_aware

a_string = "hello"
DECODE_STRINGS = True
if not hasattr(a_string, 'decode'):
    DECODE_STRINGS = False


def make_utc(dt):
    if settings.USE_TZ and is_naive(dt):
        return make_aware(dt, timezone=timezone.utc)

    return dt


def aware_utcnow():
    return make_utc(datetime.utcnow())


def datetime_to_epoch(dt):
    return timegm(dt.utctimetuple())


def datetime_from_epoch(ts):
    return make_utc(datetime.utcfromtimestamp(ts))


def format_lazy(s, *args, **kwargs):
    return s.format(*args, **kwargs)


format_lazy = lazy(format_lazy, str)
