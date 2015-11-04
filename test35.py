#ecoding: utf8
'''
Created on 2015年8月22日

@author: lizelin
'''

import os
#基本方法，利用迭代遍历给定目录的所有文件
def dirlist(path):
    listdirs=os.listdir(path)
    for dir1 in listdirs:
        dirall=os.path.join(path,dir1)
        if os.path.isdir(dirall):
            dirlist(dirall)
        print dirall
        a.append(dirall)

#利用walk来迭代遍历目录
def dirlist1(path):
    g=os.walk(path)
    for temppath,dirs,files in g:
        for i in files:
            filesall.append(os.path.join(temppath,i))
        


a=[] 
filesall=[]
dirlist('D:\\Users\\lizelin\\workspace\\python_study\\testdirs')

dirlist1('D:\\Users\\lizelin\\workspace\\python_study\\testdirs')
print filesall


