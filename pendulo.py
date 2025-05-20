# Analise do ruido nas medições de um pêndulo
# O objetivo é comparar dados experimentais com a forma analitica de calcular a gravidade atraves de um pêndulo
# Para um pêndulo simples o periodo T (tempo de oscilação completa), depende da gravidade g segundo a formula:
# T = T=2π√(L/g) onde L é o comprimento do fio
# Ruído são variações pequenas causadas nas imprecições das medidas

import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

# parâmetros do experimento
L = 1.0
g_real = 9.81
num_medidas = 1000  # número de medições

# Gerar dados com ruído
T_ideal = 2 * np.pi * np.sqrt(L/g_real)
# Medições com ruído pequeno (erro aleatório)
ruido = np.random.normal(0, 0.05, num_medidas)  # média 0, desvio 0.05s
T_medido = T_ideal + ruido

# Calcular o valor de g para cada medição
g_medido = 4 * np.pi**2 * L / T_medido**2

# Estatísticas
media = np.mean(g_medido)
mediana = np.median(g_medido)
desvio_padrao = np.std(g_medido)
q1 = np.percentile(g_medido, 25)
q3 = np.percentile(g_medido, 75)

# Exibir resultados
print(f"g (real): {g_real:.3f} m/s²")
print(f"g (média): {media:.3f} m/s²")
print(f"g (mediana): {mediana:.3f} m/s²")
print(f"Desvio padrão: {desvio_padrao:.3f} m/s²")
print(f"1º quartil (Q1): {q1:.3f}")
print(f"3º quartil (Q3): {q3:.3f}")

# Criar figura com dois subplots
plt.figure(figsize=(12, 6))

# Histograma com curva gaussiana
plt.subplot(1, 2, 1)
n, bins, patches = plt.hist(g_medido, bins=15, color='skyblue', edgecolor='black', density=True)
plt.axvline(g_real, color='red', linestyle='--', label='g real')

# Gerar a distribuição normal (gaussiana)
mu = media  # média das medições
sigma = desvio_padrao  # desvio padrão das medições
x = np.linspace(min(g_medido), max(g_medido), 1000)  # intervalo para o eixo x
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Plotar a função gaussiana
plt.plot(x, y, 'r-', linewidth=2, label='Distribuição Normal')

plt.title("Distribuição das medições de g")
plt.xlabel("g (m/s²)")
plt.ylabel("Densidade de probabilidade")
plt.legend()

# Boxplot
plt.subplot(1, 2, 2)
plt.boxplot(g_medido, vert=False)
plt.title("Boxplot das medições de g")
plt.xlabel("g (m/s²)")

# Ajustar o layout
plt.tight_layout()

# Exibir os gráficos
plt.show()

