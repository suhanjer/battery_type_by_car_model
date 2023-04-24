from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect('catalog.db')
db = conn.cursor()

wb = load_workbook('./catalog.xlsx')
legkovye = wb.active

a = []

#model = []
#model_line = []
#model_type = []
#f = []
#t = []

for cellObj in legkovye['B3':'J24713']:
    for cell in cellObj:

        if cell.value == '+++' or cell.value == '---' or cell.value == '===':
            break



        a.append(cell.value)


    if a:
        db.execute("INSERT INTO legkovye (model, model_line, model_type, f, t, ae, prem, plus, econ) VALUES (:model, :model_line, :model_type, :f, :t, :ae, :prem, :plus, :econ)", {"model": a[0], "model_line": a[1], "model_type": a[2], "f": a[3], "t": a[4], "ae": a[5], "prem": [6], "plus": [7], "econ": [8]})

    a.clear()

wb.close()

conn.commit()

conn.close()
