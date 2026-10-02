# a = (1,2,3,(4,5))
# n = len(a)
#accessing tuple using for loop and  while
# for i in range(n):
#     if type(a[i]) is tuple:
#         m = len(a[i])
#         for j in range(m):
#             print(i,j,a[i][j])
#     else:
#         print(i,a[i])
# i = 0
# while i<n:
#     if type(a[i]) is tuple:
#         j=0
        
#         m = len(a[i])
#         while j<m:
#             print(i,j,a[i][j])
#             j+=1
#         i+=1    
#     else:
#         print(i,a[i])
#         i+=1
             
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3][0])
# print(a[3][1])
# # a = (1,2)

# # b = (a,3,4,5)
# # print(b)

c = ((1,2,3),
     (4,5,6))

#without index
# for i in c:
#     for j in i:
#         print(j)
#     print()
#with index
# n = len(c)
# for i in range(n):
#     for j in range(len(c[i])):
#         print(i,j,":",c[i][j])
#     print()
i=0
#without index
# while i<len(c):
#     j=0
#     while j<len(c[i]):
#         print(c[i][j])
#         j+=1
#     i+=1
#with index
while i<len(c):
    j=0
    while j<len(c[i]):
        print(i,j,":",c[i][j])
        j+=1
    i+=1
# print(c)
# print(c[0])
# print(c[1])
# print(c[0][0])
# print(c[0][1])
# print(c[0][2])
# print(c[1][0])
# print(c[1][1])
# print(c[1][2])