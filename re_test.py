import re

x=re.findall('a.x','a xfjaxx')
print(x)

y=re.findall('^Hel','Hello nihao Hel fuk')
print(y)

z=re.findall('py$','hello.py')
print(z)

a=re.findall('[A-Z][a-z0-9]{5}','Alkj4561efiojKIOJLKs9jre9AKLJFDS98234J9D')
print(a)

b=re.findall('[a-z]+\W[0-9]+','wangming-56')
print(b)

c=re.findall('hello\s+\S+','hello peter hello alice hello julia hello andrew')
print(c)

d=re.findall('ab+','abbsdfklfabababsdfkwjfecababababawfbafbabababbbbbawab')
print(d)

e=re.findall('ab+?','abbsdfklfabababsdfkwjfecababababawfbafbabababbbbbawab')
print(e)

f=re.match('(ab)cde','abcdesdfsdfsa').group()
print(f)

g=re.match('(?P<wan>我爱你){2,5}?','我爱你我爱你我爱你我爱你').group()
print(g)

h=re.match('(?P<jhl>jhl)(?P=jhl)','jhljhljhlwwwwzz').group()
print(h)

i=re.match(r'[a-zA-Z]\w{7,9}','qf16l_wlz_').group()
print(i)

j=re.match(r'\d{17}(\d|X)','31022719970830441X').group()
print(j)

pattern=r'\w{3}[abc]\w{3}'
obj=re.compile(pattern)
k=obj.findall('45dfsbkll456dsf')
print(k)

#分割字符串
l=re.split(r'\s+','wo sdjkf fjlkw wofsdds')
print(l)

#替换字符串内容
m=re.sub(r'\s+','*','wo     shi zhen de xihuan ni a\nwo\tye\tshi o',3)
print(m)

n=re.search(r'(?P<NO1>\A[A-Z])\w*(?P<NO2>\s+\w+)','Hello world,woaini')
print(n)
print(n.start(),n.end(),n.span(),n.group(),n.groups(),n.groupdict())
print(n.pos,n.endpos,n.lastgroup,n.lastindex,n.string)

#忽略大小写
o=re.findall('abcdefg','aBCDefg',re.I)
print(o)

#点.可以匹配换行\n
p=re.findall(r'.*','wawawa\nooo',re.DOTALL)
print(p)

#^ $可以匹配一行的开头、结尾 (\A和 \Z不行)
q=re.findall(r'wao$','hhh wao\nuuu wao',re.M)
print(q)
r=re.findall(r'^yayaya','yayaya wowowow\nyayaya lllaala',re.M)
print(r)

#同时使用flags 使用|      re.M|re.I