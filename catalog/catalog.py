from openpyxl import load_workbook
import sqlite3
from datetime import datetime

conn = sqlite3.connect('catalog.db')
db = conn.cursor()

wb = load_workbook('./catalog.xlsx')
legkovye = wb.active

a = []

model = None
model_line = None
model_type = None
f = None
t = None

for cellObj in legkovye['B3':'J24713']:
    for cell in cellObj:

        if cell.value == '+++' or cell.value == '---' or cell.value == '===':
            if cell.value == '+++':
                model_line = None
                model_type = None
                f = None
                t = None
            if cell.value == "===":
                model_type = None
            break



        a.append(cell.value)

        if len(a) == 9:
            if a[0] != None:
                model = a[0]
            if a[1] != None:
                model_line = a[1]
            if a[2] != None:
                model_type = a[2]
            if a[3] != None:
                ft = '01/' + a[3]
                f = datetime.strptime(ft, '%d/%m/%y').date()
            if a[4] != None:
                tt = '28/' + a[4]
                t = datetime.strptime(tt, '%d/%m/%y').date()
            else:
                tt = '01/01/20'
                t = datetime.strptime(tt, '%d/%m/%y').date()

    if len(a) == 9:
        if a[0] == None:
            a[0] = model
        if a[1] == None:
            a[1] = model_line
        if a[2] ==  None:
            a[2] = model_type
        if a[3] == None:
            a[3] = f
        if a[4] == None:
            a[4] = t

        if a[3] != None and a[2] != None:
            db.execute("INSERT INTO legkovye (model, model_line, model_type, f, t, ae, prem, plus, econ) VALUES (:model, :model_line, :model_type, :f, :t, :ae, :prem, :plus, :econ)", {"model": a[0], "model_line": a[1], "model_type": a[2], "f": a[3], "t": a[4], "ae": a[5], "prem": a[6], "plus": a[7], "econ": a[8]})

    a.clear()

wb.close()

conn.commit()

conn.close()
