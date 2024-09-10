import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dados de exemplo (altura, peso, idade, tamanho do pé)
dados_pessoas = np.array([
    [1.75, 70, 25, 42],   # Pessoa 1
    [1.80, 85, 30, 44],   # Pessoa 2
    [1.60, 60, 22, 39],   # Pessoa 3
    [1.55, 55, 18, 37],   # Pessoa 4
    [1.90, 90, 35, 45],   # Pessoa 5
    [1.65, 65, 28, 40],   # Pessoa 6
    [1.72, 75, 32, 43],   # Pessoa 7
    [1.68, 62, 24, 41],   # Pessoa 8
])

# Normalização dos dados para evitar que uma característica domine as outras
scaler = StandardScaler()
dados_normalizados = scaler.fit_transform(dados_pessoas)

# Definindo o número de clusters (número de grupos)
kmeans = KMeans(n_clusters=3, random_state=42)

# Treinando o modelo K-Means
kmeans.fit(dados_normalizados)

# Pegando os grupos de cada pessoa (rótulos dos clusters)
grupos = kmeans.labels_

# Exibir os resultados
for i, grupo in enumerate(grupos):
    print(f"Pessoa {i+1} pertence ao grupo: {grupo}")

# Função para prever o grupo de uma nova pessoa
def prever_grupo(nova_pessoa):
    # Normalizando os dados da nova pessoa para ficar consistente com o modelo treinado
    nova_pessoa_normalizada = scaler.transform([nova_pessoa])
    # Prevê o grupo do novo dado
    grupo = kmeans.predict(nova_pessoa_normalizada)
    return grupo[0]

# Testando com uma nova pessoa
nova_pessoa = [1.77, 82, 29, 43]  # altura, peso, idade, tamanho do pé
grupo_previsto = prever_grupo(nova_pessoa)
print(f"A nova pessoa foi classificada no grupo: {grupo_previsto}")

# Plotando os clusters
plt.scatter(dados_normalizados[:, 0], dados_normalizados[:, 1], c=grupos, cmap='viridis')
plt.title('Clusterização de Pessoas com K-Means')
plt.xlabel('Altura (normalizado)')
plt.ylabel('Peso (normalizado)')
plt.show()
