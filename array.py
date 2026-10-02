import numpy as np
#from numpy import *
#
## 1.8 is the start, 5 is the end, and 50 is how many numbers you want
#a = np.ones(5,dtype = int)
#n = len(a)
#el=0
#while el<n:
#    print(a[el])
#    el+=1

#x = np.array([101,102,103,104,105])
#y = np.array([101,2,103,104,5])
#math operation
#z=x+y
#print(z)
#comparision operator
#z=x<=y
#print(z)
#any and all function
#z =x>y
#print(any(z)) #return true cuz in any function if one element fullfil the condition it's return true
#print(all(z)) #in this if all element fullfil the condition then it's return true
#where function
#z = np.where(x==y,x,y) #in this if condition is true it's return the first expersion and if false it's retuen the second# value
#print(z)
#non zero
#a = np.array([100,200,10,300,0,400,0,500])
#b = np.nonzero(a) #IT SKIP those index ehere value is zero
#print(b)
#taking inout from user in an array
n = int(input("Enter num of element in an array: "))
a = np.zeros(n,dtype=int)
#for i in range(0,len(a)):
#    x = int(input("Enter the Element of array:"))
#    a[i] = x
#el=0
#while el<n:
#    print(el,a[el])
#    el+=1
i= 0
while i<n:
    x = int(input("Enter the Element of array:"))
    a[i] = x
    i+=1
    
for b in range(n):
    print(b,a[b])
