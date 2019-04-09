import gevent
import time

def f1(a,b):
    print('halo',a)
    gevent.sleep(2)
    print('i\'m',b)

def f2():
    print('wow')
    gevent.sleep(1)
    print('hello')

g1=gevent.spawn(f1,1,2)
g2=gevent.spawn(f2)

gevent.joinall([g1,g2])