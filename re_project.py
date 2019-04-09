import re

with open(r'G:\资料类的\大学\day02\regex\1.txt','r') as f:
    text=f.read()
    msg=re.split(r'\n\n',text)
    # print(msg[1])
    for i in msg[1:]:
        x=re.match('\S+',i).group()
        try:
            y=re.findall(r'address\s+is\s+\w{4}\W\w{4}\W\d{4}',i)[0]
        except IndexError:
            y=None
        try:
            z=re.findall(r'Internet address\s+is\s+\d+\W\d+\W\d+\W\d+\W\d+',i)[0]
        except IndexError:
            z=None
        print(x,y,z)