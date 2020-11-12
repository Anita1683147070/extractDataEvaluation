import sys

sys.path.append('..')
import re
import pandas as pd


def str2date(str_date):
    str_date = re.findall('[0-9]+', str_date)
    date = '{}-{}-{}'.format(str_date[0].zfill(4), str_date[1].zfill(2), str_date[2].zfill(2))
    return date
