#!/bin/env python3

import hashlib

f = open('./exo2_data', 'r')
arr = f.read().split('\n')

for mdp in arr:
    mdp += "5UA@/Mw^%He]SBaU"
    h = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
    print(h)
    if h == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b":
        print(mdp)