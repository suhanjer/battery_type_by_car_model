import sqlite3

conn = sqlite3.connect('catalog/catalog.db')
db = conn.cursor()

db.execute('SELECT DISTINCT ae, prem, plus, econ FROM legkovye WHERE model = "ABARTH" AND model_line = "500 / 595 / 695 (312_)" AND model_type = "1.4 (99 kW)" AND t > "2019-12-30" AND f < "2019-12-30"')

models = []

for row in db:
    for r in row:
        if r != None:
            models.append(r)
    # models.append(row[0] + row[1])

print(models)

# rows = []

# for row in db.execute("SELECT DISTINCT model FROM legkovye"):
    # rows.append(row[0])
    # print(rows)

conn.close()
