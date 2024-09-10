## README para Algoritmo de Clustering

### Clustering com K-Means

**Descrição:**

O algoritmo K-Means é uma técnica de clustering que visa dividir um conjunto de dados em K clusters, onde cada ponto de dado pertence ao cluster com a média mais próxima. É amplamente utilizado para encontrar grupos naturais em dados.

**Como Funciona:**

1. **Inicialização:**
   * Seleciona K pontos iniciais como centros dos clusters (ou "centróides").
2. **Atribuição de Clusters:**
   * Cada ponto de dado é atribuído ao cluster cujo centro é o mais próximo.
3. **Atualização dos Centros:**
   * Atualiza os centros dos clusters para ser a média dos pontos atribuídos a cada cluster.
4. **Repetição:**
   * Repete a atribuição e atualização dos centros até que os centros não mudem significativamente (ou um critério de parada seja atingido).

**Código Exemplo:**

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copiar código</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dados de exemplo (altura, peso, idade, tamanho do pé)
data = np.array([
    [1.60, 50, 25, 40],
    [1.75, 65, 30, 42],
    [1.80, 70, 35, 44],
    [1.85, 80, 40, 46],
    [1.70, 60, 28, 41],
    [1.90, 90, 33, 48],
    [1.78, 75, 31, 43],
    [1.82, 68, 29, 45]
])

# Escalonamento dos dados
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Aplicar o K-Means
kmeans = KMeans(n_clusters=3, random_state=0).fit(data_scaled)
labels = kmeans.labels_
centros = kmeans.cluster_centers_

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centros[:, 0], centros[:, 1], c='red', s=200, alpha=0.75, marker='x')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Clustering com K-Means')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
</code></div></div></pre>

**Explicação do Código:**

* Normaliza os dados para garantir que cada característica tenha igual peso.
* Aplica o algoritmo K-Means para encontrar 3 clusters nos dados.
* Plota os dados escalonados e os centros dos clusters, mostrando como os pontos estão agrupados e onde estão localizados os centros dos clusters.
