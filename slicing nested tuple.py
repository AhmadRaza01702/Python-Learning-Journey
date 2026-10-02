x=((1,2,3),   #0
   (4,5,6),   #1
   (7,8,9),   #2
   (20,22,23),#3
   (10,11,12))#4
print("0 to 4 index slicing")
a = x[0:5]
print(a)
#ab agr ma ny just 2 index ko lena ho or usy get krny ky bad nested tuple ma na rkhn ho tu ye krty ha
b = x[2:3] #is sy second index wly element get ho gy
print(b)
b = x[2:3][0]#is sy senond index bahir a jye ga nested tuple sy
print(b)
#agr hm kisi specific nested tuple ky values ma sy specific value lena chaihye tu like ma khta hn 1st index waly tuple ki 2nd values just get kro
print("Get the 2nd value of 1st index tuple")
c = x[1:2][0][2]
print(c)
print("Get only second tuple values using loop")
d =x[2:3][0]
for i in d:
    print(i) 

e =x[-3:]
print(e)
f =x[-3:][1] # jo x[-3:][1] is ma 1 sy hmy pta chl rha ha jo hm ny 3 tuple last ma slice kye un ma sy jo 1st index wala tuple ha usy print kro
print(f)
g =x[-3:][1][0] # jo x[-3:][1] is ma 1 sy hmy pta chl rha ha jo hm ny 3 tuple last ma slice kye un ma sy jo 1st index wala hm ny jo get kia ha uska 0 poistion waly ki value lekho
print(g)
h = x[-3:][2]
for i in h:
    print(i) 