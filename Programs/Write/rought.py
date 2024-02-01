import pandas as pd
from datetime import datetime
import os


current = datetime.now().strftime('%m-%d-%Y_%H-%M-%S')
print(current)

path = 'C:\\Users\\lnv0176\\Downloads\\Playwright-Python_Framework.xlsx'
sheet = 'Object LocatorIdentification'
read = pd.read_excel(path , sheet_name=sheet)
print(read)

write = open(f'C:\\Users\\lnv0176\\PycharmProjects\\Learn\\Raw\\Write\\{current}.txt','w')
write.write(read.to_string())
print(write)
write.close()

append = open(f'C:\\Users\\lnv0176\\PycharmProjects\\Learn\\Raw\\Write\\{current}.txt','a')
append.write(read.to_string())
append.close()
print(append)


# file = open('C:\\Users\\lnv0176\\Downloads\\Playwright-Python_Framework.xlsx','r')
# file.read()
# print(file)
# file.close()



