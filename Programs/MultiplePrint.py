xyz = "जय श्री राम"
no = int(input("How many times you want to print? "))
for i in range(no):
    if(i % 108 == 0):
        print("|| सीता राम हनुमान ||" + str(i))
    else:
        print(xyz)