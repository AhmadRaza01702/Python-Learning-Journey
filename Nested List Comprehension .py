lst1 = []
for i in range(6,8):
    for j in range(4,7):
        lst1.append(i*j)
print(lst1)
lst = [[i*j for j in range(4,7)]for i in range(6,8)]
print(lst)