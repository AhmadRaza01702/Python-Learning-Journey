set1 = {0,1,2,3,4,5,6,7,8,9}                       
print("Actual set                                            ",set1)
print()
set2 = {i+1 for i in set1}
print("Set Comprehension only adding 1 in each element of set",set2)
print()
set3 = {i for i in range(20) if i%2==0}
print("Set Comprehension with single if",set3)
print()
set4 = {i for i in range(20) if i%2==0 if i%3==0}
print("Set Comprehension with multiple if",set4)
print()

set5 = {i if i%2==0 else'Invalid' for i in range(20)}
print("Set Comprehension with if-else",set5) #we see only 1 invalid msg cuz set can not contain same value
