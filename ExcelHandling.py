import pandas as pd
excel_sheet = pd.read_csv("C:\\Users\\LNV-56\\Downloads\\Participants for Badminton - Sheet1.csv")

print(excel_sheet)

row_num = excel_sheet.iloc[5]
print(row_num)

cell_num = excel_sheet.iloc[2]["Name"]
print((cell_num))

total_rows = len(excel_sheet)
print((total_rows))