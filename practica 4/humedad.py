# -*- coding: utf-8 -*-
"""
Created on Mon May 12 23:22:42 2025

@author: Axel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.fft import fft, fftfreq

# Datos de humedad (copiados manualmente)
humedad_valores = [
    45.49218911, 46.41986243, 46.80236419, 48.34478267, 48.36697107,
    48.14795502, 47.63336347, 45.00855045, 49.75818679, 49.89350708,
    50.61015797, 48.11102589, 49.10753861, 53.98763034, 52.41935849,
    54.48300289, 53.80146910, 54.43137747, 56.87656761, 54.59604535,
    56.44740920, 55.95544793, 56.63253875, 57.50033112, 59.17461585,
    58.37797971, 62.44451195, 58.73265369, 60.72730636, 60.79006557,
    65.12026088, 63.16351469, 65.36456232, 60.84565804, 64.85131724,
    66.58057065, 65.43277457, 67.84805094, 65.11259548, 69.37639352,
    # ... puedes agregar los valores faltantes aquí ...
]

# Crear el vector de tiempo (muestreo cada 5 segundos)
fs = 1 / 5  # Frecuencia de muestreo = 0.2 Hz
n = len(humedad_valores)
tiempo = np.arange(n) * 5  # segundos

# Convertir a DataFrame
df = pd.DataFrame({
    'Tiempo (s)': tiempo,
    'Humedad (%)': humedad_valores
})

# ----------------------
# 1. Señal original
# ----------------------
plt.figure(figsize=(10, 4))
plt.plot(df['Tiempo (s)'], df['Humedad (%)'], label='Original')
plt.title('Humedad Relativa - Señal Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Humedad (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------
# 2. Promediado móvil
# ----------------------
ventana = 3
df['Humedad_Media'] = df['Humedad (%)'].rolling(window=ventana, center=True).mean()

plt.figure(figsize=(10, 4))
plt.plot(df['Tiempo (s)'], df['Humedad (%)'], label='Original', alpha=0.5)
plt.plot(df['Tiempo (s)'], df['Humedad_Media'], label='Promediado móvil', color='red')
plt.title('Humedad Relativa - Promediado Móvil')
plt.xlabel('Tiempo (s)')
plt.ylabel('Humedad (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------
# 3. Filtro pasa bajas
# ----------------------
def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

cutoff_lp = 0.02  # Hz
b, a = butter_lowpass(cutoff_lp, fs)
humedad_lp = filtfilt(b, a, df['Humedad (%)'])

plt.figure(figsize=(10, 4))
plt.plot(df['Tiempo (s)'], df['Humedad (%)'], label='Original', alpha=0.5)
plt.plot(df['Tiempo (s)'], humedad_lp, label='Filtrado pasa bajas', color='green')
plt.title('Filtro Pasa Bajas - Humedad')
plt.xlabel('Tiempo (s)')
plt.ylabel('Humedad (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------
# 4. Filtro pasa bandas
# ----------------------
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

lowcut = 0.01  # Hz
highcut = 0.05  # Hz
b, a = butter_bandpass(lowcut, highcut, fs)
humedad_bp = filtfilt(b, a, df['Humedad (%)'])

plt.figure(figsize=(10, 4))
plt.plot(df['Tiempo (s)'], humedad_bp, label='Filtrado pasa bandas', color='purple')
plt.title('Filtro Pasa Bandas - Humedad')
plt.xlabel('Tiempo (s)')
plt.ylabel('Humedad (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ----------------------
# 5. FFT - Análisis de Frecuencia
# ----------------------
def plot_fft(signal, fs, label):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1/fs)[:N//2]
    plt.plot(xf, 2.0/N * np.abs(yf[:N//2]), label=label)

plt.figure(figsize=(10, 4))
plot_fft(df['Humedad (%)'], fs, 'Original')
plot_fft(humedad_lp, fs, 'Pasa bajas')
plot_fft(humedad_bp, fs, 'Pasa bandas')
plt.title('FFT de la señal de humedad')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()