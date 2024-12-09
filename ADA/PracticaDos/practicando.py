def knapsack(values, weights, capacity):
    
    n = len(values)
    # Crear la tabla DP (n+1 filas y capacity+1 columnas)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Rellenar la tabla de abajo hacia arriba
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Caso en el que incluimos el elemento i-1
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Caso en el que no incluimos el elemento i-1
                dp[i][w] = dp[i - 1][w]

    # El resultado está en dp[n][capacity]
    return dp[n][capacity]


# Ejemplo de uso
values = [10, 20, 30]
weights = [2, 1, 4]
capacity = 5
print("Valor máximo que se puede obtener:", knapsack(values, weights, capacity))
