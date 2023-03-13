#!/usr/bin/python3.10

import re
import sys
import pdb
def winL(x):
    # pdb.set_trace()
    cor = re.compile(r'c:\\', flags=re.IGNORECASE)
    co=re.sub(cor,'/mnt/c/',x )
    lin=co.replace('\\','/')
    print(f"linux: {lin}")
    print(f'windows: {x}')
    return lin
def pConv(pat='/mnt/'):
    if len(sys.argv)>1:
        pat=sys.argv[1]
    # print(pat)
    pats = re.search("/mnt/c/", pat)
    if pats:
        bb=pat.replace('/mnt/c/','c:\\').replace('/', '\\')
        print(f"Linux: {pat}\nWindows: {bb}")
    patx = re.search(r"c:\\", pat)
    if patx:
        winL(pat)
pConv()
