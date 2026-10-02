# these are mutable(can be changed), unordered , do not allow dupliccate keys

student ={
    "name": "Ahmad Raza",
    "age" : "22",
    "city": "Lahore",
    "Roll no" : "179"
    #"name": "Raza"  if we use same variable then the last one will use 

}
# student[101] = "Superior University"
# print(102 in student) #doing this we checked the given is already exisiting in the dictionary or not
# print(102 not in student) #the upper line return true when it exsist in the dic and this line return true when not exsist
# print(type(student))
# print(student)
# print(id(student))

# stu = student.copy()
# print(type(stu))
# print(stu)
# print(id(stu))

# print(student["city"])

# student["name"] = "Usman"
# print(student)

# student["favsubject"] = "Math"
# print(student)
#setdeafault ka kam ha ky GR key already exsist krti ha tu jo ab value di ha wo ajye uski jga lekh dy or agr key available nhi ha tu jo a key or value di ha wo insert ho jye

# student.setdefault(102,'ALi')
# print(student)
# stu =student.pop(101,'the given value is not exsist in the dictionary')
#print(student)
# print(stu)

# print(student.keys())
# print(student.values())
# print(student.items())
# student.update({"age":"15"})
# print(student)
# print(student.get("name"))

# key =(101,102,103,104)
# value = ('Ahmad Raza','python','Ali','javascrpit')
# stu = dict.fromkeys(key,value)
# print(stu)
# stu = {101:'Ahmad',102:'Raza',103:'Python'}
# print(stu)
# print()

# print(stu.keys())
#print keys
# all_keys = stu.keys()
# print(all_keys)
# print(type(all_keys))

# lst = list(all_keys)
# print(lst)
# print(type(lst))

# for i in lst:
#     print(i)

#print values
# all_values = stu.values()
# print(all_values)
# print(type(all_values))

# lst =list(all_values)
# print(lst)
# print(type(lst))

# for i in lst:
#     print(i)

# print(stu.get(101,'Ahmad Raza')) #key(101) jo is line ma ha agr wo exist kr rhi ho gi dic ma tu hmy uski vlue mily gi or agr exisit nhi kr rhi ho gi tu hmy jo default value hm ny set ki ha wo mily gi agr hm default value set na kry tu hmy none mily gi value
# it = stu.items()
# print(it)
# print(type(it))

# lst = list(it)
# print(lst)
# print(type(lst))

# print(lst[0])
# print(lst[0][0])
# print(lst[0][1])
# for r in lst:
#     for c in r:
#         print(c)
# for r in lst:
#     print(r)