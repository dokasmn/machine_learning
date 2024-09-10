## README para Modelo de Regressão Linear

### Regressão Linear para Análise de Moedas

**Descrição:**

A Regressão Linear é um método estatístico utilizado para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. No contexto de análise de valores de moedas, a regressão linear pode prever o valor futuro de uma moeda com base em dados históricos.

**Como Funciona:**

1. **Preparação dos Dados:**
   * Converte as datas para números ordinais para usar como variáveis independentes (X).
   * Utiliza os valores das moedas como variáveis dependentes (y).
2. **Treinamento do Modelo:**
   * Divide os dados em conjuntos de treinamento e teste.
   * Ajusta um modelo de regressão linear aos dados históricos para encontrar a melhor linha que minimiza o erro quadrático médio (MSE).
3. **Previsões:**
   * Usa o modelo treinado para prever valores futuros com base em datas futuras.
4. **Visualização:**
   * Plota os dados históricos, a linha de regressão ajustada e as previsões futuras em um gráfico.

**Código Exemplo:**

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copiar código</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Dados fictícios de valores do dólar
data = {
    'Data': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Valor_Dolar': [5.30, 5.28, 5.25, 5.20, 5.18, 5.15, 5.10, 5.08, 5.05, 5.03, 5.00, 4.95]
}

# Criar DataFrame
df = pd.DataFrame(data)
df['Data_Ordinal'] = df['Data'].map(pd.Timestamp.toordinal)

# Definir variáveis
X = df[['Data_Ordinal']]
y = df['Valor_Dolar']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Previsões
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# Previsões futuras
future_dates = pd.date_range(start='2024-01-01', periods=6, freq='M')
future_dates_ordinal = future_dates.map(pd.Timestamp.toordinal)
future_X = np.array(future_dates_ordinal).reshape(-1, 1)
future_predictions = model.predict(future_X)

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.scatter(df['Data'], y, color='blue', label='Dados Históricos')
plt.plot(df['Data'], model.predict(X), color='red', linestyle='--', label='Linha de Regressão')
plt.plot(future_dates, future_predictions, color='green', linestyle='--', marker='o', label='Previsões Futuras')
plt.xlabel('Data')
plt.ylabel('Valor do Dólar')
plt.title('Previsão do Valor do Dólar')
plt.legend()
plt.grid(True)
plt.show()
</code></div></div></pre>

**Explicação do Código:**

* Cria um DataFrame com dados fictícios e converte datas para números ordinais.
* Treina um modelo de regressão linear com os dados históricos.
* Faz previsões para datas futuras e plota os resultados para visualização.
