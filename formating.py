#print("********int********")
#print("{} {}".format(10,20))
#print("{1}".format(10,20))
#print("{0} {1}".format(10,20))  
#print("{1} {0}".format(10,20))
#print("{num1} {num2}".format(num1=10,num2=20))
#print("********float********")
#print("{} {}".format(10.1,20.8))
#print("{1}".format(10.1,20.8))
#print("{0} {1}".format(10.4,20.5))  
#print("{num1} {num2}".format(num1=10,num2=20.5))
#print("********string********")
#print("My name is {} {}".format("Ahmad","Raza"))
#print("{1}".format("Ahmad","Raza"))
#print("{0} {1}".format("Ahmad","Raza")) 
#print("{1} {0}".format("Ahmad","Raza"))
#print("{num1} {num2}".format(num1="Ahmad",num2="Raza"))
##we can combine int flat and string
#
#print("Define type firstly Int")
#print("{} {}".format(10,20))
#print("{:d} {}".format(10,20))
#print("{1:d} {0:d}".format(10,20))
#print("{0:f} {1:d}".format(10.1,20))
#
##aligment
#print("{0:5d}".format(10)) #ye output ma 5 block bnye ga or usy most left ma assign kr dy ga
#print("{0:05d}".format(10)) #same ha bas sapces ki jga 0 lekh dy ga
#print("{0:+5d}".format(10)) #hm + ki jga kuch bhi lekh skty ha 0 hm ny lekh kr dekh leya ha
##print("{0:*5d}".format(10)) error #imp hm * ko directly d ky sath nhi use kr skty hm isy < > ^ in ky sath use kr skty ha 
#print("{0:-5d}".format(10))
#print("{0:>5d}".format(10))
#print("{0:<5d}".format(10))#ye value ko left side per align krta ha or d ky sath jo 5 ha wo width ha
#print("{0:^5d}".format(10)) #asas
#print("{num:5d}".format(num=10))
#print("{num:05d}".format(num=10))
#print("{num:+5d}".format(num=10))
#print("{num:-<5d}".format(num=10))
#print("{num:*<5d}".format(num=10))
#print("{num:#<5d}".format(num=10)) # ase hm koi bhi charactor use kr skty ha space ko fill krny ky lye
#print("{num:#^5d}".format(num=10))
# :[fill][align][sign][#][0][width][,][.precision]type



#FLOAT
#print("{0:10f}".format(10.15)) 
#print("{0:010f}".format(10.15)) 
#print("{0:+10f}".format(10.15))
#print("{0:-10f}".format(10.15))
#print("{0:>10f}".format(10.15))
#print("{0:<10f}".format(10.15))
#print("{0:^10f}".format(10.15)) 
#print("{num:10f}".format(num=10.15))
#print("{num:010f}".format(num=10.15))
#print("{num:+10f}".format(num=10.15))
#print("{num:-<10f}".format(num=10.15))
#print("{num:*<10f}".format(num=10.15))
#print("{num:#<10f}".format(num=10.15)) 
#print("{num:#^20f}".format(num=10.15))
#print("{num:10.3f}".format(num=10.15)) #IS SY HM YE DEFINE KR KY HA KY HMY . KY BAD JUST 3 VALUES CHAIHYE
#print("{num:#^10.2f}".format(num=10.15))     


#STRING
#print("{0:8s}".format("Ahmad"))  #sting by deafault left align hota ha bki right hoty ha
#print("{0:08s}".format("Ahmad")) 
#print("{0:.3s}".format("Ahmad")) #ase ye phl .3 charactor reD KRY GA 
#print("{0:8.3s}".format("Ahmad"))
#print("{0:*<8.3s}".format("Ahmad")) # hm without < > ^ koi special charactor use nhi kr skty
#
#print("{0:>8s}".format("Ahmad"))
#print("{0:<8s}".format("Ahmad"))
#print("{0:*^8s}".format("Ahmad"))
#print("{0:*>8s}".format("Ahmad"))
#print("{0:*<8s}".format("Ahmad"))

print("Some extra and imp concept")
print("{0:,}".format(1234567890)) #thousand speration ky lye use hota ha _ bhi same ha
print("{0:_}".format(1234567890))

name = "Ahmad Raza"
age = 22
print("My name is {} and age is {}.".format(name,age)) # yha per upper waly sare operation perform kr skty ha jase upper kye ha {} ma 
a=50
b=3
print("{:.2}".format(a/b))
print("{:.2%}".format(a/b))

value = (10,20)
#print("{} {}".format(value)) #error
print("{0[0]} {0[1]}".format(value)) #[] is phly wla 0 hmry variable value ko denote kr rha ha cuz wo format ka 1st variable ka index 0 hota ha tu wo 0 value ky index ko show kr rha

data1 = {'Ahmad':2000, 'Raza':3000}
print("{0[Ahmad]:>100d} {0[Raza]:d}".format(data1))
print("{a[Ahmad]:>10d} {a[Raza]:d}".format(a=data1))
print("{Ahmad:>10d} {Raza:5d}".format(**data1))