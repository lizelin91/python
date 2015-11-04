#encoding: utf-8
'''
Created on 2015年8月21日

@author: lizelin
'''

import os
import time
import re
from lib2to3.fixer_util import String

'''
os.mkdir('t34')  #创建目录
time.sleep(2)
os.makedirs('a/b/c')
os.rmdir('t34')
print os.listdir('.')
'''

'''
print os.getcwd()
os.chdir('C:/')
os.mkdir('lizelin')
print os.getcwd()
'''

'''
#创建四个目录，其中一个目录中有一个文件
os.mkdir('f1')
os.mkdir('f2')
os.mkdir('f3')
os.mkdir('jpg')
path=os.getcwd()
f=open(path+'/jpg/getjpg.py','w')
f.close()
'''


def showfiles(path):
    rule=r'.*\..+?'
    dircount=0
    filescount=0
    pathlist=os.listdir(path)
    for i in pathlist:
        if re.match(rule,i)!=None :
            if cmp(i,'.settings')==0:
                dircount+=1
            else:
                filescount+=1
        elif re.match(rule,i)==None:
            dircount+=1
    print '%s directory, %s files' %(dircount,filescount)


print os.getcwd()
path=raw_input('please input path:\n')
showfiles(path)



'''path=os.getcwd()
print os.listdir(path)
'''
