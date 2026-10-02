print("1 to 10 counting: ")
c = 1

while c<=10 :
    print(c)
    c=c+1
print("10 to 1 counting: ")
b = 10
while b>0:
    print(b)
    b=b-1
print("even num:")
a=1
while a<50:
    if a%2==0:
     print(a)
     a=a+1
    else: 
       a=a+1

print("SUM OF N NUM:")

d = int(input("Enter a num: "))
a=1
sum=0
while a<=d:
   sum= sum+a
   a=a+1

print("sum of n num is:",sum)

print("\t shape Question")
k = int(input("Enter a num: "))
x = 1

while x<=4:
   print("*" * x)
   x=x+1

print("\t Enter name 5 time")
a=input("Enter your name: ")
i = 1
while i<=5:
   print(i,". ",a)
   i=i+1
print("\tTable")
z =int(input("Enter a num for the table: "))
j=1
while j<=10:
   print(z,"*",j ,"= ", j*z)
   j=j+1
