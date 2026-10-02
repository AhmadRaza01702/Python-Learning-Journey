from array import *

def show(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)
a = array('i',[101,102,103,104,105])
show(a)


def show(ar):
    print("passd array:",ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar
a = array('i',[101,102,103,104,105])
y = show(a)
print("Returing array",y)
print(type(y))
for i in y:
    print(i)
