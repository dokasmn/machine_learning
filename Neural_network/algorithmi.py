import numpy as np

# Função de ativação - degrau (step function)
def step_function(x):
    return 1 if x >= 0 else 0

# Classe para o Perceptron
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        # Inicializando os pesos com valores pequenos aleatórios
        self.weights = np.random.rand(input_size + 1)  # +1 para o bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    # Função de treinamento
    def train(self, training_inputs, labels):
        for epoch in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                # Adiciona o bias (1) ao vetor de entrada
                inputs_with_bias = np.append(inputs, 1)
                
                # Cálculo da soma ponderada
                weighted_sum = np.dot(inputs_with_bias, self.weights)
                
                # Função de ativação
                prediction = step_function(weighted_sum)
                
                # Atualizando os pesos
                self.weights += self.learning_rate * (label - prediction) * inputs_with_bias

    # Função de previsão
    def predict(self, inputs):
        # Adiciona o bias (1) ao vetor de entrada
        inputs_with_bias = np.append(inputs, 1)
        weighted_sum = np.dot(inputs_with_bias, self.weights)
        return step_function(weighted_sum)

# Exemplo de dados de entrada (usando a função AND)
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])  # Saída da função lógica AND

# Criando o Perceptron
perceptron = Perceptron(input_size=2)

# Treinando o Perceptron
perceptron.train(training_inputs, labels)

# Testando o Perceptron
print("Testando o Perceptron:")
for inputs in training_inputs:
    print(f"Entrada: {inputs}, Saída prevista: {perceptron.predict(inputs)}")
