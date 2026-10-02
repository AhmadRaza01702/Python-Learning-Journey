a = [1,2,3,4,5,6,7,8,9,10]

print(a)
def even(n):
    if n%2==0:
        return True
result = filter(even,a)
for i in result:
    print(i)