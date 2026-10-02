a = 50
def show():
    a = 10
    print('A:',a)

show()
print(a)
# agr golabal keyword use when our local and floabal vaiable name are same
# also in this if we change the value then golobal and local both value are changed

i = 10
def s():
    global i
    i = i+1
    print(i)

s()
print(i)

#gloabal function

a = 50
def show():
    a = 10
    x= globals()['a']

    print('A:',a)
    print('X:',x)

show()
print(a)