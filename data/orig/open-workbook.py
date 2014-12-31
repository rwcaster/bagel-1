import xlrd
book = xlrd.open_workbook('Bagel Data Reporting.xlsx')

print [ line for line in book ] 
