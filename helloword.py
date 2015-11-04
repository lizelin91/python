# -*- coding: cp936 -*-
from __future__ import division  #除法包，使得5/2等于2.5
#coding: cp936
def add(x,y):
    return x+y
def mine(x,y):
    return x-y
def ch(x,y):
    return x*y
def div(x,y):
    return x/y

def operator(x,o,y):
    if o=='+':
        print add(x,y)
    elif 0=='-':
        print mine(x,y)
    elif o=='*':
        print ch(x,y)
    elif o=='/':
        print div(x,y)
    else :
        pass

op={'+':add,'-':mine,'*':ch,'/':div}
def f(x,o,y):
    print op.get(o)(x,y)
 
if __name__=='__main__':
    f(5,'/',3)
#f(3,'*',9)
