import pandas as pd
import numpy as np

def leer_datos(excel_file):
    # Leemos el archivo Excel
    df = pd.read_excel(excel_file)
    
    df['Costo_Facebook'] = df['Costo_Facebook'].fillna(0)
    df['Costo_Google'] = df['Costo_Google'].fillna(0)
    
    anuncios = df['Anuncio'].tolist()
    costos_facebook = df['Costo_Facebook'].tolist()
    impactos_facebook = df['Impacto_Facebook'].tolist()
    costos_google = df['Costo_Google'].tolist()
    impactos_google = df['Impacto_Google'].tolist()
    
    return anuncios, costos_facebook, impactos_facebook, costos_google, impactos_google

def asignacion_anuncios(anuncios, costos_facebook, impactos_facebook, costos_google, impactos_google, presupuesto_facebook, presupuesto_google):
    n = len(anuncios)
    
    presupuesto_facebook = int(presupuesto_facebook)
    presupuesto_google = int(presupuesto_google)
    
    costos_facebook = [int(costo) for costo in costos_facebook]
    costos_google = [int(costo) for costo in costos_google]
    
    dp = np.zeros((n + 1, presupuesto_facebook + 1, presupuesto_google + 1))
    
    for i in range(1, n + 1):
        for j in range(presupuesto_facebook + 1):
            for k in range(presupuesto_google + 1):
                dp[i][j][k] = dp[i-1][j][k]
                
                if j >= costos_facebook[i-1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-costos_facebook[i-1]][k] + impactos_facebook[i-1])
                
                if k >= costos_google[i-1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-costos_google[i-1]] + impactos_google[i-1])
    
    valor_maximo_ventas = dp[n][presupuesto_facebook][presupuesto_google]
    
    asignaciones = {'Facebook': [], 'Google': []}
    anuncios_no_asignados = []  
    j, k = presupuesto_facebook, presupuesto_google
    for i in range(n, 0, -1):
        if dp[i][j][k] == dp[i-1][j][k]:
            anuncios_no_asignados.append(anuncios[i-1])  # Anuncio no asignado
            continue
        else:
            if dp[i][j][k] == dp[i-1][j-costos_facebook[i-1]][k] + impactos_facebook[i-1]:
                asignaciones['Facebook'].append((anuncios[i-1], impactos_facebook[i-1]))
                j -= costos_facebook[i-1]
            else:
                asignaciones['Google'].append((anuncios[i-1], impactos_google[i-1]))
                k -= costos_google[i-1]

    return valor_maximo_ventas, asignaciones, anuncios_no_asignados

def main():
    excel_file = 'anuncios.xlsx' 
    anuncios, costos_facebook, impactos_facebook, costos_google, impactos_google = leer_datos(excel_file)

    presupuesto_facebook = 1000 
    presupuesto_google = 1200
    
    valor_maximo_ventas, asignaciones, anuncios_no_asignados = asignacion_anuncios(
        anuncios, costos_facebook, impactos_facebook, costos_google, impactos_google, presupuesto_facebook, presupuesto_google)
    
    print(f"Valor máximo de ventas: {valor_maximo_ventas}")
    
    print("\nAsignación de anuncios a Facebook:")
    for anuncio, impacto in asignaciones['Facebook']:
        print(f"- {anuncio}: {impacto} ventas")
    
    print("\nAsignación de anuncios a Google:")
    for anuncio, impacto in asignaciones['Google']:
        print(f"- {anuncio}: {impacto} ventas")
    
    print("\nAnuncios no asignados a ninguna plataforma:")
    if anuncios_no_asignados:
        for anuncio in anuncios_no_asignados:
            print(f"- {anuncio}")
    else:
        print("No hay anuncios no asignados.")

if __name__ == "__main__":
    main()
