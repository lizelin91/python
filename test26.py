import re
s=r'tkp'
s1=r'top'
s2=r't[io]p'
s3=r't[^io]p'
s4=r'^top'
s5=r'\^abc'
s6=r'010-[0-9]{8}'
s7=r'^010-*\d{8}$'
s8=r'010-?\d{8}'
l='^abc uji top ok good kisd tkp ttopp tip tkp'
num='010-12345678 010-87654321'
ss8=re.findall(s8, num)

ps=re.compile(s8)
print ps.findall(num)
x=ps.match(num)
print x.group()

print re.split(r'[/+-/*//]','234+786-7634/2134*89')