#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
x=-30
n=10
xi=-np.pi
xf=-xi
delt=0.1

def func(x):
 return x

def anbn(xi,xf,n):
 an=0
 bn=0
 i=xi+delt
 while(i<=xf):
  an=an+(func(i-delt)*np.cos(n*(i-delt))+func(i)*np.cos(n*i))*delt/2
  bn=bn+(func(i-delt)*np.sin(n*(i-delt))+func(i)*np.sin(n*i))*delt/2
  i=i+delt
 return an,bn

def Calca0(xi,xf):
 i=xi
 a0=0
 while(i<=xf):
  a0=a0+(func(i-delt)+func(i))*delt/2
  i=i+delt
 return a0
fourier=[]
while(x<30):
 val=0
 for i in xrange(0,n+1):
  an,bn=anbn(xi,xf,i)
  val=an*np.cos(i*x)+bn*np.sin(i*x)
 fourier.append(Calca0(xi,xf)+val)

filewrite=open('saida.dat', 'w')

for i in xrange(0, len(fourier)+1):
 filewrite.write(str(fourier[i])+"\n")

