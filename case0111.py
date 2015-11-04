import re

regg=r'src="(.*?\.jpg)'
strr='http://static.tieba.baidu.com/tb/editor/images/client/image_emoticon25.png" ><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=ac9b2d17163853438ccf8729a312b01f/6fb10f2442a7d93351243a08ab4bd11373f0013b.jpg'
result=re.finditer(regg, strr)
print result
li=[1,2,3]
print li[1]