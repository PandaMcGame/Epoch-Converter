from calendar import timegm
from datetime import datetime

def convert_epoch(time):
    """Convert Epoch to Human Time"""
    return datetime.fromtimestamp(float(time)/1000).strftime('%Y-%m-%d %H:%M:%S.%f')


def convert_human():
    """Conert Human Time to Epoch"""
    return calendar.timegm(datetime.datetime.now().timetuple())
