import openpyxl

book = openpyxl.load_workbook('chuy.xlsx')

sheet = book.active

arreglos = []

rangos = ['A1:K1', 'A2:K2']

for rango in rangos:
    rango_horizontal = sheet[rango]

    arreglo_temporal = []

    for fila in rango_horizontal:
        for celda in fila:
            arreglo_temporal.append(celda.value)

    arreglos.append(arreglo_temporal)

for i, arreglo in enumerate(arreglos, start=1):
    print(f"Arreglo {i}: {arreglo}")
