a = [5,1,6,9]
b = a.copy()
print(a)
print(b)
print('After modify a')
a[1]=55
print('A',a)
print('B',b)
print('After modify b')
b[1]=65
print('A',a)
print('B',b)
print()
#cloning
print('Cloning Method')
a = [5,1,6,9]
b = a[:]
print(a)
print(b)
print('After modify a')
a[1]=55
print('A',a)
print('B',b)
print('After modify b')
b[1]=65
print('A',a)
print('B',b)