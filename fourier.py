#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

n=3
xi=-np.pi
x=xi
xf=-xi
delt=0.1

def func(x):
 return np.exp(-x**2)

def anbn(xi,xf,n):
 an=0
 bn=0
 i=xi+delt
 while(i<=xf):
  an=an+(func(i-delt)*np.cos(n*(i-delt)*np.pi/(xf-xi))+func(i)*np.cos(n*i)*np.pi/(xf-xi))*delt/2
  bn=bn+(func(i-delt)*np.sin(n*(i-delt)*np.pi/(xf-xi))+func(i)*np.sin(n*i)*np.pi/(xf-xi))*delt/2
  i=i+delt
 an=an/(xf-xi)
 bn=bn/(xf-xi)
 return an,bn

def Calca0(xi,xf):
 i=xi+delt
 a0=0
 while(i<=xf):
  a0=a0+(func(i-delt)+func(i))*delt/2
  i=i+delt
 return a0/(xf-xi)

fourier=[]
filewrite=open('saida.dat', 'w')

while(x<xf):
 val=0
 for i in xrange(0,n+1):
  an,bn=anbn(xi,xf,i)
  val=val+an*np.cos(i*x*np.pi/(xf-xi))+bn*np.sin(i*x*np.pi/(xf-xi))
 print x
 fourier.append(Calca0(xi,xf)/2+val)
 x=x+delt
 filewrite.write(str(x)+'   '+str(fourier[-1])+'\n')
