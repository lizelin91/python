#coding: utf-8

path='D:/Users/lizelin/workspace/hello/'
f0=open(path+'test32.txt')
print f0.read()
f0.close()

print '#'*5

f1=file(path+'test32.txt')
print f1.read()
f1.close()



fnew=open(path+'new.txt','w')
fnew.write('hello lusi \n i am new\n this is ok')
fnew.close()

'''
f2=open(path+'new.txt','r+')
f2.read()
f2.write('new context again')
f2.close()
'''

#利用a来追加

f3=open(path+'new.txt','a')
f3.write('\na new string')
f3.close()
