import os
import json

__author__ = 'jwkim'
'''
any comments?
'''

cur_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(
    cur_dir,
    'cldb.ini',
)

with open(json_path) as fin:
    fin = json.load(fin)

cldb_url = fin['cldb']['url']
