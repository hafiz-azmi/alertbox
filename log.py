import pandas as pd
from clock import date, time
import os

this_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(this_dir, 'work.csv')

def log_in():
    row = {'date': [date()], 'in':[time()], 'out':['tbd']}
    df = pd.DataFrame(row, columns=['date', 'in', 'out'])
    df = df.set_index('date')
    df.to_csv(file_path, mode='a', header=False)

def log_out():
    df = pd.read_csv(file_path, index_col='date', names=['date', 'in', 'out'])
    df.at[date(), 'out'] = time()
    df.to_csv(file_path, header=False)
