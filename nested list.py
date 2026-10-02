# #  0 1 2 34[0]4[1]
# b = [50,60]
# a=[1,2,3,4,b]#valid

# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(a[3])
# # print(a[4][0])
# # print(a[4][1])

# n = len(a)
# i=0
# while i<n:
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m = len(a[i])
#             j=0
#             while j<m:
#                 print(i,j,a[i][j])
#                 j = j+1
#             i = i+1
#     else:
#         print(i,a[i])
#         i+=1
            

# for i in range(n):
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#              print(i,j,a[i][j])
#     else:
#         print(i,a[i])















#
# c=[10,20,30,40,b] #also valid

# d = [[11,12,13],[22,23,24]] # valid

# x = [21,31,34]
# y = [51,52,53]
# z=[x,y]
# print('A',a)
# print('C',c)
# n = len(c)
# for i in range(n):
#     print(i,c[i])
# print('B',b)
# print('C',c)
# print('D',d)
# print('X',x)
# print('Y',y)
# print('Z',z)
# d = [[11,12,13],[22,23,24]]
x = [11,12,13]
y = [22,23,24]
z = [x,y]
#Without index

# for i in d:
#     for j in i:
#         print(j)
#     print()

#with index
n = len(z)
for i in range(n):
    for j in range(len(z[i])):
        print(i,j,z[i][j])

i =0 
while i<n:
    j = 0
    while j<len(z[i]):
        print(i,j,z[i][j])
        j+=1
    i+=1

