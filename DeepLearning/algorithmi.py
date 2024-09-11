# Importando bibliotecas necessárias
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Gerando dados fictícios
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Dividindo os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando a Rede Neural Profunda
model = Sequential()
model.add(Dense(64, input_dim=1, activation='relu'))  # Camada oculta com 64 neurônios
model.add(Dense(32, activation='relu'))               # Outra camada oculta com 32 neurônios
model.add(Dense(1))                                   # Saída com 1 neurônio (valor contínuo)

# Compilando o modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Treinando o modelo
model.fit(X_train, y_train, epochs=100, verbose=1)

# Avaliando o modelo
loss = model.evaluate(X_test, y_test)
print(f"Perda (MSE) no teste: {loss}")

# Fazendo previsões
y_pred = model.predict(X_test)

# Plotando os resultados
import matplotlib.pyplot as plt
plt.scatter(X_test, y_test, color='blue')
plt.scatter(X_test, y_pred, color='red')
plt.xlabel('X (Feature)')
plt.ylabel('y (Target)')
plt.title('Rede Neural Profunda')
plt.show()
