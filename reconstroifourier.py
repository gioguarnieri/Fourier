#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
xi=-np.pi

fileread=open('teste2.dat','r')
ak=[]
bk=[]
x=[xi]
y=[]

for line in fileread:
 xj,yj,k=line.split()
 ak.append(float(xj))
 bk.append(float(yj))
delt=(np.pi-xi)/len(ak)

aux1=max(ak)/1000
aux2=max(bk)/1000

for i in xrange(0,len(ak)):
 if(aux1>ak[i]):
  ak[i]=0
 if(aux2>bk[i]):
  bk[i]=0

while(x[-1]<=np.pi):
 soma=0
 for i in xrange(0,len(ak)):
  soma=soma+ak[i]*np.cos(2*np.pi*i*x[-1]/len(ak))+bk[i]*np.sin(2*np.pi*i*x[-1]/len(bk))
 soma=soma/len(ak)
 y.append(soma) 
 print x[-1], y[-1]
 x.append(x[-1]+delt)
