import random
count =0
number = random.randint(1,10)
print(number)
while count < 3:
    num = int(input("Enter your number: "))
    if(number==num):
       print("Correct Guess")
       break
    elif(abs(number-num==1)):
        print("close")
    elif(abs(number-num>1)):
        print("not close")
    else:
       print("Wrong Guess")
    count = count+1