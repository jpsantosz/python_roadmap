import numpy as np

temperaturas = np.array([
     27.5, 28.6, 30.0, 27.5, 27.5, 27.5, 26.9, 26.9, 28.9, 29.4,
    25.8, 26.9, 28.3, 30.6, 30.6, 28.6, 28.6, 29.2, 28.1, 28.1,
    28.1, 29.2, 26.9, 28.1, 26.9, 26.9, 27.9, 26.4, 26.9, 26.4
])

temperatura_media = np.average(temperaturas)
temperatura_max = np.max(temperaturas)
temperatura_min = np.min(temperaturas)
desvio_padrao = np.std(temperaturas)

print(f"A temperatura média foi {temperatura_media:.2f}")
print(f"A temperatura máxima foi {temperatura_max:.2f}")
print(f"A tempertaura mínima foi {temperatura_min:.2f}")
print(f"O desvio padrão é {desvio_padrao:.2f}")

above_thirty = temperaturas[temperaturas > 30]

print(f"Dias a cima de 30°: {above_thirty}")

temperaturas_normalizadas = (temperaturas - temperatura_min) / (temperatura_max - temperatura_min)

print(f"Temperaturas normalizadas: {temperaturas_normalizadas}")