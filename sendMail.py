#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender='lizelin_lzl@163.com'
receiver='362378878@qq.com'
subject='python test mail'
smtpsever='smtp.163.com'
username='lizelin_lzl@163.com'
password='lzl@612321'
content='hello this a test mail. sorry to trouble you.'
msg=MIMEText(content,'plain','utf-8')
msg['Subject']='测试邮件'
msg['To']=receiver

smtp=smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()