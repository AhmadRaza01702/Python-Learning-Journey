import numpy as np
#by using these function we can create multi-d-array
#1. arry() 2. zeros() 3. ones() 4. reshape() 
##1. array():
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
 
print(a.ndim)#ndim represent the dimesion of an array
print(a.shape)
print(a.size)
print(a.itemsize)#represent size in bytes
print(a.dtype)
#formula :print(a.size*a.itemsize)#represent nbytes total num of bytes
print(a.nbytes)

#n = a[0:2,1:3]
#print(n)
#n = len(a)
#print(n)
##for r in range(n):
##    for c in range(len(a[r])):
##        print(r,c,":",a[r][c])
##    print()
#r = 0
#
#while r<n:  # 0<5 TRUE
#    c= 0 
#   #len(a[r]) represent how many column are in the array
#    while c<len(a[r]): # 0<5 , 1<5
#        print(r,c,":",a[r][c])
#        c+=1 #c=0 sy 1
#    r+=1 # r=1
#    print()
#2. zeros():
#a = np.zeros((3,2))
#n = len(a)
#print(a)
#3. ones()
#a = np.ones((3,2),int)
#n = len(a)
#for r in range(n):
#    for c in range(len(a[r])):
#      print(r,c,":",a[r][c])
#    print()
#4. reshape()
#a = np.array([1,2,3,4,5,6])
#b = np.reshape(a,(2,3))
#print(b)
# 5. flatten() used to convert 2d or 3d array to 1d array
#a = np.array([[10,20,30,40,50],
#              [60,70,80,90,100]])
#b =a.flatten()
#print(a)
#print(b)

#r= int(input("Enter your rows:"))
#c = int(input("Enter your column:"))
#a = np.zeros((r,c),int)
#u = len(a)
##print(a)
##for i in range(u):
##    for j in range(len(a[i])):
##        x = int(input("Enter your number:"))
##        a[i][j] = x
##for i in range(u):
##    for j in range(len(a[i])):
##        print(i,j,":",a[i][j])
##    print()
##print(a)
#i =0
#
#
#while i<u:
#    j = 0
#    while j< len(a[i]):
#        x = int(input("Enter your number:"))
#        a[i][j] = x
#        j+=1
#    i+=1
#
#i=0
#while i<u:
#    j = 0
#    while j< len(a[i]):
#        print(i,j,":",a[i][j])
#        j+=1
#    i+=1
#
#print(a)