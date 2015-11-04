#coding:utf-8
'''
Created on 2015年8月23日

@author: lizelin
'''
filename=raw_input('请输入要打开的文件!')
try:
    open(filename)
    print ' try'
except IOError,msg:
    print '文件不存在'
finally:
    print 'zuihou'

    
print 'good'