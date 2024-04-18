from openpyxl import Workbook
wb= Workbook()

ws= wb.active

#ws['A1']= "Country"
testdata= [['Name','Country'],['Joey','USA'], ['Sam','UK']]
for data in testdata:
    ws.append(data)
wb.save("test.xlsx")