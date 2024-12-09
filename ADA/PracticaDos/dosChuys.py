def knapsack_multidimensional(values_fb, values_gg, costs_fb, costs_gg, capacity_fb, capacity_gg):
    n = len(values_fb)

    # Crear la tabla DP con dimensiones (n+1) x (capacity_fb+1) x (capacity_gg+1)
    dp = [[[0] * (capacity_gg + 1) for _ in range(capacity_fb + 1)] for _ in range(n + 1)]

    # Rellenar la tabla
    for i in range(1, n + 1):
        for fb in range(capacity_fb + 1):
            for gg in range(capacity_gg + 1):
                # No incluir el anuncio i-1
                dp[i][fb][gg] = dp[i - 1][fb][gg]

                # Incluir el anuncio en Facebook si hay presupuesto
                if costs_fb[i - 1] <= fb:
                    dp[i][fb][gg] = max(dp[i][fb][gg], dp[i - 1][fb - costs_fb[i - 1]][gg] + values_fb[i - 1])

                # Incluir el anuncio en Google si hay presupuesto
                if costs_gg[i - 1] <= gg:
                    dp[i][fb][gg] = max(dp[i][fb][gg], dp[i - 1][fb][gg - costs_gg[i - 1]] + values_gg[i - 1])

    # Backtracking para encontrar los objetos seleccionados
    fb, gg = capacity_fb, capacity_gg
    selected_fb = []  # Anuncios seleccionados para Facebook
    selected_gg = []  # Anuncios seleccionados para Google

    for i in range(n, 0, -1):
        # Si el valor no cambió, el anuncio no se incluyó
        if dp[i][fb][gg] == dp[i - 1][fb][gg]:
            continue

        # Si el anuncio se incluyó en Facebook
        if fb >= costs_fb[i - 1] and dp[i][fb][gg] == dp[i - 1][fb - costs_fb[i - 1]][gg] + values_fb[i - 1]:
            selected_fb.append(i - 1)  # Guardar el índice del anuncio
            fb -= costs_fb[i - 1]  # Reducir el presupuesto disponible en Facebook
        # Si el anuncio se incluyó en Google
        elif gg >= costs_gg[i - 1] and dp[i][fb][gg] == dp[i - 1][fb][gg - costs_gg[i - 1]] + values_gg[i - 1]:
            selected_gg.append(i - 1)  # Guardar el índice del anuncio
            gg -= costs_gg[i - 1]  # Reducir el presupuesto disponible en Google

    # El resultado estará en dp[n][capacity_fb][capacity_gg]
    max_value = dp[n][capacity_fb][capacity_gg]
    return max_value, selected_fb, selected_gg


# Datos del problema
values_fb = [300, 500, 450, 650, 250, 550, 350, 400, 330, 600]
values_gg = [350, 600, 500, 750, 200, 650, 450, 300, 370, 770]
costs_fb = [200, 300, 250, 400, 150, 350, 250, 220, 180, 320]
costs_gg = [250, 350, 300, 450, 200, 400, 280, 250, 200, 350]
capacity_fb = 1000
capacity_gg = 1200

# Llamar a la función
resultado, seleccion_fb, seleccion_gg = knapsack_multidimensional(
    values_fb, values_gg, costs_fb, costs_gg, capacity_fb, capacity_gg
)

# Convertir índices de 0-based a 1-based
seleccion_fb_humana = [x + 1 for x in seleccion_fb]
seleccion_gg_humana = [x + 1 for x in seleccion_gg]

print("Valor máximo que se puede obtener:", resultado)
print("Facechuy", seleccion_fb_humana)
print("Chuygle:", seleccion_gg_humana)
