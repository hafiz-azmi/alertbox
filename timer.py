import time

def timer(hour=0, minute=0, second=0):
    hour_sec = hour * 60 * 60
    min_sec = minute * 60
    clock = hour_sec + min_sec + second
    time.sleep(clock)
    return 0
