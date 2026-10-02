a = set()
print(type(a))
n = int(input("Enter the total element of set: "))

for i in range(n):
    el = input("Enter value of you set:")
    a.add(el)
print(a)
for i in a:
    print(i)