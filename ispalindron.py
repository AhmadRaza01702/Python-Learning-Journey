
#b = int(input("Enter a value: "))
#length = len(str(abs(b)))
#c=0
#z=b
#print("actual num: ",b)
#while length!=0:
#    length=length-1
#    a = b%10
#    b=int(b/10)
#    c= c+(a*(10**length))
#print("Revers", c)
#if (z==c):
#    print("Palindrone")
#else:
#    print("not Palindrone")
#
a = input("Enter a num: ")

# negative index sy complete string print krna 
c= a[-len(a):]
print(c)
# :: is used to revered the string 
b = a[::-1]

print(b)

if (a==b):
    print("Palindrone")
else:
    print("not Palindrone")
