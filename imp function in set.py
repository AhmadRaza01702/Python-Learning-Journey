a = {1,2,3,4,5,6,'Ahmad Raza','Ali'}
b = {11,12,4,5,'Ali',8,9,7}
print("A:",a)
print("B:",b)
c = a.intersection(b)
print("Intersection of A and B:",c)
d = a.union(b)
print("Union of A and B",d)
e = a.difference(b)
print("Difference of A and B:",e)
f  = a.issubset(b)
print("IS A is the subset of B:",f) #subset ka mtlb ky phly set ky all elemnt second set ma exsist krty ha ya nhi
g = a.issuperset(b) #agr b ky all element a ma exisit krty ho gy tu true return kry ga
print("Is A is the super set of B:",g)