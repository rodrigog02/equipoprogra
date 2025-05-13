# -*- coding: utf-8 -*-
"""
Created on Mon May 12 23:33:36 2025

@author: Axel
"""

import pandas as pd
import matplotlib.pyplot as plt

# Datos manuales basados en la imagen (puedes reemplazar esto por la lectura de un archivo CSV)
data = {
    'Tiempo': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Temperatura_C': [
        25.248357076505616, 25.244820447060974, 25.95051043687187,
        26.698421501132636, 26.126372748462607, 26.428016493400147,
        27.630229171177085, 27.512613822401818, 27.1740311775411,
        27.950413996687963
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar las primeras filas
print(df.head())

# Graficar los datos
plt.figure(figsize=(10, 5))
plt.plot(df['Tiempo'], df['Temperatura_C'], marker='o', linestyle='-')
plt.title('Temperatura vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()