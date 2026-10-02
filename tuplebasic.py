#list can be changed and tuple canot be changed 

# name = ("Ahmad", "Usman", "Ali","Usman")
# print(name)

# print(type(name))

# emptytuple = ()
# singletuple = (1, )

# print(type(emptytuple))
# print(type(singletuple))

# print(name.index("Usman"))
# print(name.count("Usman"))
# a =(10,20,30,40,50)
# print(a)

# c = (101,102)
# s1 = a[0:2]
# s2 = a[2:]
# modifytuple = s1+c+s2
# print(modifytuple)

# #for repitation
# b = (1,2,3)
# r = b*3
# print(r)

#we can copy tuple element using slicing also if the data of orginal tuple reamin same in the copy tuple then it's remain same fo this we can not copy the all data of orignal tuple
a = (1,2,3,4,5,6)
b = a[1:6]
print("A:",a)
print(id(a))
print('B:',b)
print(id(b))