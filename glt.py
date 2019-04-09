import greenlet

def f1():
    print('first')
    g2.switch()
    print('second')
    g2.switch()

def f2():
    print('third')
    g1.switch()
    print('fourth')
    g1.switch()

g1=greenlet.greenlet(f1)
g2=greenlet.greenlet(f2)
g1.switch()