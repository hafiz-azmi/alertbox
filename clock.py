import datetime

def date():
    now = datetime.datetime.now()
    datex = now.strftime("%d/%m/%Y")
    return datex

def time():
    now = datetime.datetime.now()
    timex = now.strftime("%H:%M:%S")
    return timex
