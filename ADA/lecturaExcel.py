import openpyxl

book = openpyxl.load_workbook(('prueba_escritura.xlsx'))

sheet=book.active

a1=sheet['A1']
a2=sheet['A2']

print(a1.value)
print(a2.value)
print(type(a1.value))