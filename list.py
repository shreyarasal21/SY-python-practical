list=[1,2,4,4,5,]
print(list)
list.append(21)
print(list)
list.insert(2,3)
print(list)
list[2]=10
print(list)
list.extend([1,4,2])
print(list)
print(list[2])
list.remove(4)
print(list)
list.pop(4)
print(list)
list.pop()
print(list)
del list[1]
print(list)
print(len(list))
if 4 in list:
    print("element is present")
else:
    print("not present")

for i in list:
 print(i)

 print(list.count(4))

 
 print(list.index(4))

 list.sort()
 print(list)

 list.sort( reverse = True)
 print(list)

 new_list=list.copy()
 print(new_list)

 list.clear()
 print(list)
 