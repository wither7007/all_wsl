#!/bin/usr/python3.10
##c reads bigc from (from bash fd c:\ function) and sorts by mb
bg=[line.strip() for line in open('/mnt/c/all/bigC') if not 'denied' in line.strip() ]
myf=[a.split(' ')[4:] for a in bg]
mult = dict(K=2**10, M=2**20, G=2**30)
def mysize(line):
    value=line[0]
    nvalue=float(value[:-1])
    unit=value[-1]
    final=nvalue*mult[unit]
    return final
myf.sort(key=mysize,reverse=True)
finalMy=[f'{a[0]} {a[-1]}' for a in myf]
open('/mnt/c/all/finalSize.txt', 'w', encoding='utf-8').write('\n'.join(finalMy))
'''
allBigs(){
  #general find bigg file
(cd /mnt/c && fdi --size +30m -x ls -lhrt  > /mnt/c/all/bigC 2>&1 &)
}
'''
