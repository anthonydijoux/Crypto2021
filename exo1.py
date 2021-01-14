#!/bin/env python3

import hashlib

f = open('./db', 'r')
arr = f.read().split('\n')

for mdp in arr:
    h = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
    if h == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b":
        print(mdp)