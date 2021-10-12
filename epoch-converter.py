import time

def convert_epoch(time):
    return datetime.fromtimestamp(float(time)/1000).strftime('%Y-%m-%d %H:%M:%S.%f')
