from isodate import Duration, duration_isoformat
from typing import Iterator
import logging
from enum import Enum

logger = logging.getLogger('atlasapi.lib')


class AtlasUnits(Enum):
    SCALAR_PER_SECOND = 'SCALAR_PER_SECOND'
    SCALAR = 'SCALAR'
    PERCENT = 'PERCENT'
    MILLISECONDS = 'MILLISECONDS'
    BYTES = 'BYTES'
    GIGABYTES = 'GIGABYTES'
    BYTES_PER_SECOND = 'BYTES_PER_SECOND'
    MEGABYTES_PER_SECOND = 'MEGABYTES_PER_SECOND'
    GIGABYTES_PER_HOUR = 'GIGABYTES_PER_HOUR'


class AtlasGranularities(object):
    """Helper class to create ISO 8601 durations to pass to the API

    To add more possible granularities, add them here.

    """
    MINUTE = duration_isoformat(Duration(minutes=1))
    FIVE_MINUTE = duration_isoformat(Duration(minutes=5))
    HOUR = duration_isoformat(Duration(hours=1))
    DAY = duration_isoformat(Duration(days=1))


class AtlasPeriods(object):
    """Helper class to create ISO 8601 durations to send to the Atlas period parameter.

    To add more periods, add them here.
    """
    MINUTES_15 = duration_isoformat(Duration(minutes=15))
    HOURS_1 = duration_isoformat(Duration(hours=1))
    HOURS_8 = duration_isoformat(Duration(hours=8))
    HOURS_24 = duration_isoformat(Duration(hours=24))
    HOURS_48 = duration_isoformat(Duration(hours=48))
    WEEKS_1 = duration_isoformat(Duration(weeks=1))
    WEEKS_4 = duration_isoformat(Duration(weeks=4))
    MONTHS_1 = duration_isoformat(Duration(months=1))
    MONTHS_2 = duration_isoformat(Duration(months=2))
    YEARS_1 = duration_isoformat(Duration(years=1))
    YEARS_2 = duration_isoformat(Duration(years=2))


# noinspection PyCallByClass
class _GetAll(object):
    is_leaf = False

    @classmethod
    def get_all(cls) -> Iterator[str]:
        out = cls.__dict__
        for item in out:
            if '_' not in item and not item[0].isupper():
                yield cls.__getattribute__(cls, item)
            elif '_' not in item and item[0].isupper():
                sub_out = cls.__getattribute__(cls, item).__dict__
                for sub_item in sub_out:
                    if '_' not in sub_item and not sub_item[0].isupper():
                        yield cls.__getattribute__(cls, item).__dict__.get(sub_item)
                    if '_' not in sub_item and sub_item[0].isupper():
                        sub_sub_out = cls.__getattribute__(cls, item).__dict__.get(sub_item).__dict__
                        for sub_sub_item in sub_sub_out:
                            if '_' not in sub_sub_item and not sub_sub_item[0].isupper():
                                yield sub_sub_out.get(sub_sub_item)


class _GetAllLeaf(_GetAll):
    is_leaf = True



