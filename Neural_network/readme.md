## README para Rede Neural Simples

### Rede Neural Simples

**Descrição:**

Uma Rede Neural Simples é um modelo de aprendizado de máquina inspirado no funcionamento do cérebro humano. Consiste em camadas de neurônios (ou unidades), onde cada neurônio em uma camada está conectado a cada neurônio na camada seguinte. Redes neurais podem ser usadas para uma variedade de tarefas, incluindo classificação e regressão.

**Como Funciona:**

1. **Preparação dos Dados:**
   * Dados de entrada são preparados e normalizados.
2. **Construção da Rede:**
   * Define a arquitetura da rede neural, incluindo camadas de entrada, ocultas e de saída.
   * Cada camada tem pesos que são ajustados durante o treinamento.
3. **Treinamento:**
   * Usa um conjunto de dados para treinar a rede, ajustando os pesos através de um algoritmo de otimização (como o gradiente descendente) para minimizar o erro.
4. **Avaliação:**
   * Avalia o desempenho da rede com dados de teste e ajusta conforme necessário.

**Código Exemplo:**

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copiar código</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

# Dados de exemplo (altura, peso) e valores de saída (rendimento)
X = np.array([[1.60, 50], [1.75, 65], [1.80, 70], [1.85, 80]])
y = np.array([2000, 2500, 2700, 3000])

# Criar e treinar o modelo de rede neural
model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000, activation='relu', solver='adam')
model.fit(X, y)

# Fazer previsões
X_test = np.array([[1.70, 60], [1.90, 90]])
y_pred = model.predict(X_test)

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], y, color='blue', label='Dados Históricos')
plt.scatter(X_test[:, 0], y_pred, color='red', marker='x', label='Previsões')
plt.xlabel('Altura (m)')
plt.ylabel('Rendimento ($)')
plt.title('Previsão de Rendimento com Rede Neural')
plt.legend()
plt.grid(True)
plt.show()
</code></div></div></pre>

**Explicação do Código:**

* Define e treina uma Rede Neural Simples (MLPRegressor) com dados fictícios de entrada e saída.
* Faz previsões com novos dados e plota os resultados.
