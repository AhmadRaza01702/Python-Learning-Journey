from numpy import *



print("THIS IS THE NUMPY FILE")
def show(ar):
    print("passd array:",ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar
a = array([101,102,103,104,105])
print(a)
y = show(a)
print("Returing array",y)
print(type(y))
for i in y:
    print(i)