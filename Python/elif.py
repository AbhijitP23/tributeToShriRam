
x = float(input('Enter marks - '))

#print(marks)

if x>=0 and x<35:
    print('Fail')

elif x>=35 and x<60:
    print('Average')

if x>=60 and x<=75:
    print('Good.')

elif x>75 and x<90:
    print('Distict.')

elif  x>=90 and x<=100:
    print('|| सीता राम हनुमान ||')

elif x<0 and x>100:
    print('Enter Valid Inputs')

else:
    print('Enter Valid Input')