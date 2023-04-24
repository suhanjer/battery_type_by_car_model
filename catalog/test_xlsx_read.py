from openpyxl import load_workbook
import time

wb = load_workbook('catalog.xlsx')
legkovye = wb.active

a = []

for cellObj in legkovye['B3':'J24713']:
    for cell in cellObj:

        if cell.value == '+++' or cell.value == '---' or cell.value == '===':
            break

        a.append(cell.value)

    if a:
        print(a)

    a.clear()
    print(len(a))

wb.close()
