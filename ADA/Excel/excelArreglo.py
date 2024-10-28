import openpyxl

book = openpyxl.load_workbook('chuy.xlsx')#cargar el archivo de Excel

sheet = book.active#se selecciona la hoja activa

rango_horizontal1 = sheet['A1:K1']#rango de celdas desde A1 hasta K1 (rango horizontal)
rango_horizontal2 = sheet['A2:K2']
rango_horizontal3 = sheet['A3:K3']
rango_horizontal4 = sheet['A4:K4']
rango_horizontal5 = sheet['A5:K5']

arreglo1=[]
arreglo2=[]
arreglo3=[]
arreglo4=[]
arreglo5=[]


for fila in rango_horizontal1:#iterar a través del rango y agregar los valores al arreglo
    for celda in fila:
        arreglo1.append(celda.value)

for fila in rango_horizontal2:
    for celda in fila:
        arreglo2.append(celda.value)


# Imprimir el arreglo con los valores
print(arreglo1)
print(arreglo2)
