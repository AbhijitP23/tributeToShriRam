import pandas as pd
import os
from datetime import datetime

live = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
print(live)

# fileName = live.strftime('%d-%m-%Y_%H-%M-%S')
#
# print(fileName)

path = 'C:\\Users\\lnv0176\\Downloads\\Playwright-Python_Framework.xlsx'
sheet = 'Test Case'
read = pd.read_excel(path, sheet_name=sheet)
print(read)

o = open(f'C:\\Users\\lnv0176\\PycharmProjects\\Learn\\Raw\\Write\\{live}.txt','w')
o.write(read.to_string())
o.close()

# app = open(f'C:\\Users\\lnv0176\\PycharmProjects\\Learn\\Raw\\Write\\{live}.txt','a')
# app.write(read.to_string())
# print(app)
# app.close()

# a = open('C:\\Users\\lnv0176\\PycharmProjects\\Learn\\Raw\\Write\\29-01-2024_19-49-10.txt','r')
#
# r = a.read()
#
# print(r)