# a = {'course':'Python','fee':15000,1:{'course':'javascript','fee':10000}}

# print(a)
# print(a['course'])
#  print(a['fee'])
#  print(a[1])
# print(a[1]['course'])
#  print(a[1]['fee'])
# a['course'] = 'Machine Learning' #yha hm ny python ki value chang ki
# print(a['course'])
# print(a)
# #ab agr ma chata hn ky nested dic ki fee ya koi bhi value change ho

# a[1]['fee'] = 20000
# print(a[1]['fee'])
# print(a)

# del a[1]['fee']
# print(a)

# adding new value
# a['duration'] = '6 month'
# print(a)

# a[1]['teacher'] = 'Geekyshow'
# print(a)
# add new dic
# a[2] = {'course':'Reactjs','fee':30000}
# print(a)
# #agr hm dic ky andar koi dic add krna chaty ha tu
# a[1][2] = {'course':'Reactjs','fee':30000}
# print(a)

# for i in a:
#     if type(a[i]) is dict:
#         for k in a[i]:
#             print(k,'=',a[i][k])
#     else:
#         print(i,':',a[i])

a = {1:{'course':'javascript','fee':10000},2:{'course':'Python','fee':15000},3:{'course':'Reactjs','fee':30000}}
print("OUTER KEYS:")
for id in a:
    print(id)
print()
print('INSIDE KEYS:')
for id in a:
    for key in a[id]:
        print(key)
print()
print("ALL INSIDE KEYS AND VALUES:")
for key in a:
    print(a[key])
print()
print('INSIDE KEYS WITH VALUES:')
for id in a:
    for key in a[id]:
        print(key,":",a[id][key])
print()
print("ALL DICTIONARY KEYS AND VALUES(INSIDE KEYS  AND OUTER KEYS):")
for id in a:
    print(id,a[id])