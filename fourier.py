#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
def akbk(x, y, k):
 ak=0
 bk=0
 for xj,yj in zip(x,y):
  ak=ak+yj*np.cos(k*xj)
  bk=bk+yj*np.sin(k*xj)
 ak=ak/m
 bk=bk/m
 return ak,bk

fileread=open(sys.argv[-1],'r')

x=[]
y=[]

for line in fileread:
 xi,yi=line.split()
 x.append(float(xi))
 y.append(float(yi))
m=len(x)
for i in xrange(0,40):
 xj,yj=akbk(x,y,i)
 print xj,yj, i
del x, y 

