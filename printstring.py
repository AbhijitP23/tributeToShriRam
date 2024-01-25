str1 = "जय श्री राम"
no = int(input("How many times you want to print? "))
for i in range(no):
    if(i % 108 == 0):
        print(str(i) + "|| सीता राम हनुमान ||")
    else:
        print(str1)
