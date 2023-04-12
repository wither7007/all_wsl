#!/usr/bin/python3.10
#link
import re
import pdb
import sys
import os
myos = sys.platform
print("Current OS: ", myos)
mydir=os.getcwd()
# print(mydir)
cor = re.compile(r'c:\\', flags=re.IGNORECASE)
def winL(x):
    # pdb.set_trace()
    co=re.sub(cor,'/mnt/c/',x )
    lin=co.replace('\\','/')
    print(f"cd {lin}")
    print(f'cd {x}')
    return lin
def pConv(pat=mydir+'/'):
    if len(sys.argv)>1:
        pat=sys.argv[1]
    # print(f'pat: {pat}')
    pats = re.search("/mnt/c/", pat)
    if pats:
        bb=pat.replace('/mnt/c/','c:\\').replace('/', '\\')
        print(f"cd {pat}\ncd {bb}")
    patx = re.search(cor, pat)
    if patx:
        winL(pat)
pConv()
