#coding: utf-8
import re
import string
'''
Created on 2015年8月18日

@author: lizelin
'''

'''
path='D:/Users/lizelin/workspace/hello/'
f=open(path+'new.txt','a')
l=['\none\n','two\n','three\n']
f.writelines(l)

f.flush()
'''

'''
path='D:/Users/lizelin/workspace/hello/'
f=open(path+'a.t')
strr=f.read()
rules=r'hello'
listt=re.findall(rules,strr)
print len(list)
f.close()
'''

'''
path='D:/Users/lizelin/workspace/hello/'
f1=open(path+'a.t')
str1=f1.read()
str2=str1.replace('hello','csvt')
f1.close()

f2=open(path+'a2.t','w')
f2.write(str2)
f2.close()
'''


path='D:/Users/lizelin/workspace/hello/'
f=open(path+'a.t','r+')
str1=f.read()
str2=str1.replace('hello','csvt')
f.seek(0,0)
f.truncate()
f.write(str2)
f.close()

