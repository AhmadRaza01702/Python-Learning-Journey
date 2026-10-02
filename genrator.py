#genrator is used to return sequence of values using yield
# def display(a,b):
#     yield a
#     yield b
# result = display(10,20)
# print(result)
# print(type(result))
# # lst = list(result) #convert it into list for prinet the values
# # print(lst)
# # print(type(lst))



# #now we add next function ehich retuen us the genrator function values using this we can not need to cnovert it into list
# print(next(result))
# print(next(result))

def shpw(a,b):
    while a<=b:
        yield a
        a+=1
result = shpw(1,5)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
