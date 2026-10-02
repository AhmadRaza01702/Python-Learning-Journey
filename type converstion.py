#their are two type of type coversition
#1. implicit conversion(automatic)  convert small data type into large to prevert the loss like covert int into float automatic
#2. Explicit conversion(manual)  covert small into large and large into small manually by describing the data type like convert str into int by describing the data type
#implicit example
x=5 #int
y=1.5 #float

z= x+y #float in this x convert into float this is implicit conversion
print(z)

a=int(input("Enter the value ")) #convert str into int by describing the datatype
print(a)
print("Datatype of Z is ", type(z))
print("Datatype of a is ", type(a))