#List Comprehension without if
lst = [0,1,2,3,4,5,6,7,8,9,10]
# print("Before any List Comprehension:"),lst
# new_lst = [i+1 for i in lst]
# print("List Comprehension without if:",new_lst)
# new_lst = [i for i in lst if i%2==0]
# print("List Comprehension one if:",new_lst)
# new_lst = [i for i in lst if i%2==0 if i%3==0]
# print("List Comprehension multiple if:",new_lst)

# new_lst = [i for i in lst if i%2!=0 if i%3!=0]
# print("List Comprehension multiple if:",new_lst)
new_lst = [i if i%2==0 else 'num is not divisible' for i in lst]
print("List Comprehension if else statement:",new_lst)