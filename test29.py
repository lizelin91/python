import re
email=r"\w{3}@\w+\.com|\w{3}@\w+\.cn"

print re.findall(email,'liz@dfc.com')

 
