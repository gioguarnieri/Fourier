#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

per=20
i=0
xi=-per
xf=per
delt=0.01
m=(xf-xi)/delt
def func3(x):
 return np.sin(np.pi*x/1000)*np.sin(20*np.pi*x/1000)

def func2(x):
 if x>10:
  return 1.
 elif x==10:
  return 0.5
 else:
  return -1.

def func1(x):
 if x>0:
  return 1.
 elif x==0:
  return 0.5
 else:
  return -1.
 
def akbk(x, y, k):
 ak=0
 bk=0
 for xj,yj in zip(x,y):
  ak=ak+yj*np.cos(k*xj)
  bk=bk+yj*np.sin(k*xj)
 ak=ak/m
 bk=bk/m
 return ak,bk


def faztudo(nome):
 xd=[xi]
 x=[]
 y=[]
 while(xd[-1]<=xf):
  y.append(nome(xd[-1]))
  x.append(-np.pi+(xd[-1]-xi)/xf*np.pi)
  xd.append(xd[-1]+delt)
  #print x[-1], y[-1]

 for i in xrange(1,11):
  xj,yj=akbk(x,y,i)
  print xj,yj, i
 print ''
 print ''
 del x, y, xd

faztudo(func1)
faztudo(func2)
faztudo(func3)
