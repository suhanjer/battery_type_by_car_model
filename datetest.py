from datetime import datetime

a = '11/81'
b = '12/87'
c = '01/83'

date = datetime.strptime(a, '%m/%y').date()

print(type(date))
print(date)
