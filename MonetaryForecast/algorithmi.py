import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Dados de exemplo (datas e valores do dólar em relação ao real)
# Para um modelo real, você deve usar dados históricos reais
# Exemplo de dados fictícios
data = {
    'Data': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Valor_Dolar': [5.30, 5.28, 5.25, 5.20, 5.18, 5.15, 5.10, 5.08, 5.05, 5.03, 5.00, 4.95]
}

# Criar DataFrame
df = pd.DataFrame(data)
df['Data_Ordinal'] = df['Data'].map(pd.Timestamp.toordinal)  # Converter datas para números

# Definir variáveis independentes (X) e dependentes (y)
X = df[['Data_Ordinal']]
y = df['Valor_Dolar']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# Gerar previsões para o futuro
future_dates = pd.date_range(start='2024-01-01', periods=6, freq='M')
future_dates_ordinal = future_dates.map(pd.Timestamp.toordinal)
future_X = np.array(future_dates_ordinal).reshape(-1, 1)
future_predictions = model.predict(future_X)

# Plotar os resultados
plt.figure(figsize=(10, 6))

# Dados históricos
plt.scatter(df['Data'], y, color='blue', label='Dados Históricos')

# Previsões
plt.plot(df['Data'], model.predict(X), color='red', linestyle='--', label='Linha de Regressão')

# Previsões futuras
plt.plot(future_dates, future_predictions, color='green', linestyle='--', marker='o', label='Previsões Futuras')

plt.xlabel('Data')
plt.ylabel('Valor do Dólar')
plt.title('Previsão do Valor do Dólar')
plt.legend()
plt.grid(True)
plt.show()
