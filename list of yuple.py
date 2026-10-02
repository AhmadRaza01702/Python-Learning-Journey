# a = (1,2,3,[4,5])
# print(a)
# print(type(a))
# n = len(a)
# for i in range(n):
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j,':',a[i][j])
#     else:
#         print(i,':',a[i])

#here we can modify the list which is inside the tuple, also we can not modify tuple 
# a[3][0] = 90
# print("After modify list inside the tuple:",a)

a = ([1,2,3],[4,5,6])
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j,':',a[i][j])

