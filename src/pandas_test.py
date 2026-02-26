import pandas as pd
import numpy as np

# 1. Creamos el dataset de ejemplo
data = {
    'Vendedor': ['Ana', 'Ana', 'Ana', 'Beto', 'Beto', 'Carlos', 'Carlos'],
    'Monto_Venta': [100, 150, 600, 200, 250, 300, 350]
}

print(data)
print(data.keys())

df = pd.DataFrame(data)

print(df)

# --- DIFERENCIA 1: .mean() (Agregación) ---
# Esto reduce el dataset. Útil para un resumen rápido.
resumen_promedios = df.groupby('Vendedor')['Monto_Venta'].mean()

print("--- RESULTADO DE .mean() ---")
print(resumen_promedios)
print(f"Tamaño del resultado: {len(resumen_promedios)} filas\n")

# --- DIFERENCIA 2: .transform('mean') (Transformación) ---
# Esto mantiene el tamaño original. Útil para Feature Engineering.
df['Promedio_Vendedor'] = df.groupby('Vendedor')['Monto_Venta'].transform('mean')

print("--- RESULTADO DE .transform() ---")
print(df)
print(f"Tamaño del resultado: {len(df)} filas")