import win32api
import time
import datetime
import pandas as pd
import os

def timer(hour=0, minute=0, second=0):
    hour_sec = hour * 60 * 60
    min_sec = minute * 60
    clock = hour_sec + min_sec + second
    time.sleep(clock)
    return 0

def log_in():
    row = {'date': [date()], 'in':[times()], 'out':['tbd']}
    df = pd.DataFrame(row, columns=['date', 'in', 'out'])
    df = df.set_index('date')
    df.to_csv(file_path, mode='a', header=False)

def log_out():
    df = pd.read_csv(file_path, index_col='date', names=['date', 'in', 'out'])
    df.at[date(), 'out'] = times()
    df.to_csv(file_path, header=False)

def date():
    now = datetime.datetime.now()
    datex = now.strftime("%d/%m/%Y")
    return datex

def times():
    now = datetime.datetime.now()
    timex = now.strftime("%H:%M:%S")
    return timex

def alert(header, message):
    win32api.MessageBox(0, message, header)

this_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(this_dir, 'work.csv')

log_in()
timer(0, 0, 2)
log_out()
alert('Work Timer', 'Your time has exhausted!')
