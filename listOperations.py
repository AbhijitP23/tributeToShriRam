

x=[1,2,3,4]
print("Total Elements", len(x));

lst = [1,5,8,8,10,58,5,0,5]
print('Original List',lst)

print('Length of List -',len(lst))

lst[0],lst[-1] = lst[-1],lst[0]
print('Replacing first and last -',lst)

lst.sort()
print('Ascending Order - ',lst)

lst.sort(reverse=True)
print('Descending Order -',lst)

print('Addition of elements- ',sum(lst))

print('occurrence',lst.count(5))

lst1 = ['a','b','c','d']

l = lst+lst1
print(l)
