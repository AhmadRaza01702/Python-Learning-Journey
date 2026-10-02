# # food ={"Burger", "pizza", "shawarma", "Sandwitch","Burger" }
# # print(type(food))

# # print(food)

# # food.add("tandori Chicken")
# # print(food)

# # food.remove('shawarma')
# # print(food)

# # #empty set
# # name = set()
# # print(type(name))
a = {1,2,3,4,'Ahmad Raza'}
# print("Before adding",a)
# print(type(a))
# a.update([4,5,6,'Ali'])
# print("After update",a)

# a.discard(4) #discard bhi remove hi krta ha element but yha error nhi milta agr jo value delete ky lye di ha wo set ma na ho
# print(a)

# for i in a:
#     print(i)
# print("Before Copy",a)
# print(id(a))
# b = a.copy()
# print("After Copy",b)
# print(id(b))

print("Before clear",a)
print(id(a))

a.clear()
print("After Clear",a)
print(id(a))