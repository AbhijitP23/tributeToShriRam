list = [23, 45, 67, 45, 87, 43]
print("Total number of element: ",len(list))
list[0],list[-1]=list[-1],list[0]
print(list)
sum =0
for i in list:
    sum =sum + i
print("sum of the element in list: ", sum)

list[2]="apple"
print("replaced list: ",list)

print("occ of num: ",list.count(45))

list2 = [56, 566, 778, 666]
#list.append(list2)
l1 = list + list2
print("concatinated list",l1)
