l1 = int(input("How many number you want to add in list? "))
list =[]
for num in range(l1):
    no= int(input("Enter no you want to add: "))
    list.insert(num,no)
print(list)