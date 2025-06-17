import pandas as pd

# Datos conocidos
meses = ['Mayo', 'Junio', 'Julio']
ventas = [70000, 80000, 100000]
ventas_previas = [60000, 70000, 80000]  # Ventas del mes anterior
saldo_inicial = 5000
otros_ingresos = 2000
compras = [50000, 70000, 80000]
renta = 3000
dividendos = [0, 3000, 0]  # Dividendos en Junio

# Calcular Entradas de Efectivo
ventas_efectivo = [v * 0.2 for v in ventas]
cuentas_cobrar_1mes = [ventas_previas[i] * 0.6 for i in range(len(meses))]
cuentas_cobrar_2meses = [ventas_previas[i-1] * 0.2 if i > 0 else 50000 * 0.2 for i in range(len(meses))]
total_entradas = [ventas_efectivo[i] + cuentas_cobrar_1mes[i] + cuentas_cobrar_2meses[i] + otros_ingresos for i in range(len(meses))]

# Calcular Desembolsos de Efectivo
sueldos_salarios = [ventas_previas[i] * 0.1 for i in range(len(meses))]
total_desembolsos = [compras[i] + renta + sueldos_salarios[i] + dividendos[i] for i in range(len(meses))]

# Calcular Saldo Final
saldo_iniciales = [saldo_inicial]
prueba_saldos = []

for i in range(len(meses)):
    saldo_neto = saldo_iniciales[-1] + total_entradas[i] - total_desembolsos[i]
    prestamos = 5000 - saldo_neto if saldo_neto < 5000 else 0
    saldo_final = saldo_neto + prestamos
    saldo_iniciales.append(saldo_final)
    prueba_saldos.append({'Saldo Neto': saldo_neto, 'Préstamos': prestamos, 'Saldo Final': saldo_final})

# Crear DataFrame
entradas_df = pd.DataFrame({
    'Concepto': ['Ventas en Efectivo (20%)', 'Cuentas por Cobrar (1 mes)', 'Cuentas por Cobrar (2 meses)', 'Otros Ingresos', 'Total de Entradas'],
    'Mayo': [ventas_efectivo[0], cuentas_cobrar_1mes[0], cuentas_cobrar_2meses[0], otros_ingresos, total_entradas[0]],
    'Junio': [ventas_efectivo[1], cuentas_cobrar_1mes[1], cuentas_cobrar_2meses[1], otros_ingresos, total_entradas[1]],
    'Julio': [ventas_efectivo[2], cuentas_cobrar_1mes[2], cuentas_cobrar_2meses[2], otros_ingresos, total_entradas[2]]
})

desembolsos_df = pd.DataFrame({
    'Concepto': ['Compras', 'Renta', 'Sueldos y Salarios', 'Dividendos', 'Total de Desembolsos'],
    'Mayo': [compras[0], renta, sueldos_salarios[0], dividendos[0], total_desembolsos[0]],
    'Junio': [compras[1], renta, sueldos_salarios[1], dividendos[1], total_desembolsos[1]],
    'Julio': [compras[2], renta, sueldos_salarios[2], dividendos[2], total_desembolsos[2]]
})

saldo_df = pd.DataFrame({
    'Concepto': ['Saldo Inicial', '+ Entradas de Efectivo', '- Desembolsos de Efectivo', 'Saldo Neto', 'Préstamos Necesarios', 'Saldo Final'],
    'Mayo': [saldo_inicial, total_entradas[0], total_desembolsos[0], prueba_saldos[0]['Saldo Neto'], prueba_saldos[0]['Préstamos'], prueba_saldos[0]['Saldo Final']],
    'Junio': [prueba_saldos[0]['Saldo Final'], total_entradas[1], total_desembolsos[1], prueba_saldos[1]['Saldo Neto'], prueba_saldos[1]['Préstamos'], prueba_saldos[1]['Saldo Final']],
    'Julio': [prueba_saldos[1]['Saldo Final'], total_entradas[2], total_desembolsos[2], prueba_saldos[2]['Saldo Neto'], prueba_saldos[2]['Préstamos'], prueba_saldos[2]['Saldo Final']]
})

# Exportar a Excel con hojas separadas
with pd.ExcelWriter('presupuesto_caja.xlsx') as writer:
    entradas_df.to_excel(writer, sheet_name='Entradas de Efectivo', index=False)
    desembolsos_df.to_excel(writer, sheet_name='Desembolsos de Efectivo', index=False)
    saldo_df.to_excel(writer, sheet_name='Saldo de Caja', index=False)

print("El archivo 'presupuesto_caja.xlsx' ha sido generado exitosamente.")
