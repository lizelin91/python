#coding:utf-8
'''
Created on 2015年8月24日

@author: lizelin
'''

class people:
    age=0
    name=''
    def speak(self):
        print 'hello'
        
man=people()
man.age=5
man.name='lize'
man.speak()
print man.age
     