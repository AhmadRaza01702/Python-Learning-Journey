a = {}

n = int(input("Enter num of dictionaryelement:"))

for i in range(n):
    k = input("Enter key:")
    v = input("Enter values:")
    a.update({k:v})

print(a)

for i in a:
    print(i,':',a[i])