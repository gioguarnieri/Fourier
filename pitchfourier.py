#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

i=0
 
def akbk(x, y, k):
 ak=0
 bk=0
 for xj,yj in zip(x,y):
  ak=ak+yj*np.cos(k*xj)
  bk=bk+yj*np.sin(k*xj)
 ak=ak/m
 bk=bk/m
 return ak,bk


x=[-np.pi]
y=[]
fileread=open("pitch.txt", 'r')

for line in fileread:
 y.append(float(line))
m=len(y)/2+1

delt=2*np.pi/len(y)
while(x[-1]<=np.pi):
 x.append(x[-1]+delt)


for i in xrange(1,m):
 xj,yj=akbk(x,y,i)
 print xj,yj, i
print ''
print ''
del x, y

