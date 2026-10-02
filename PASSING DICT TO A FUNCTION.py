#passing dictionary to a function
def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k,":",d[k])

dict = {101:'Ahmad',102:'Raza',103:'ALi'}
show(dict)
#Returning Dictionary from Function
def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k,":",d[k])
    return d
dict = {101:'Ahmad',102:'Raza',103:'ALi'}
return_dict=show(dict)
print(return_dict)
print(type(return_dict))