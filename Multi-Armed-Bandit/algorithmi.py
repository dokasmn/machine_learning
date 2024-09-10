import numpy as np

# Definindo o ambiente: 4 máquinas com probabilidades diferentes de dar uma recompensa
true_probs = [0.2, 0.5, 0.75, 0.35]  # Probabilidade de recompensa para cada máquina

# Configurações
n_arms = len(true_probs)   # Número de máquinas (braços)
n_steps = 1000             # Número de jogadas (passos)
epsilon = 0.1              # Fator de exploração (ε-greedy)

# Inicializando as estimativas de recompensa de cada braço e contadores
reward_estimates = np.zeros(n_arms)  # Estimativa inicial de 0 para todas as máquinas
action_counts = np.zeros(n_arms)     # Contagem de jogadas em cada máquina

# Função para simular o retorno de uma máquina (0 ou 1 com base na probabilidade verdadeira)
def pull_arm(arm):
    return 1 if np.random.random() < true_probs[arm] else 0

# Função ε-greedy para escolher uma máquina (exploração vs. exploração)
def choose_arm():
    if np.random.random() < epsilon:  # Exploração: escolher aleatoriamente
        return np.random.randint(n_arms)
    else:  # Exploração: escolher a máquina com maior recompensa estimada
        return np.argmax(reward_estimates)

# Simulação do aprendizado
for step in range(n_steps):
    # Escolher uma máquina com a estratégia ε-greedy
    arm = choose_arm()
    
    # Puxar a alavanca da máquina escolhida e obter a recompensa (0 ou 1)
    reward = pull_arm(arm)
    
    # Atualizar contagem de jogadas na máquina
    action_counts[arm] += 1
    
    # Atualizar a estimativa de recompensa para a máquina usando a média incremental
    reward_estimates[arm] += (1 / action_counts[arm]) * (reward - reward_estimates[arm])

# Resultados após o treinamento
print("Estimativas finais de recompensa para cada máquina:")
for i in range(n_arms):
    print(f"Máquina {i+1}: {reward_estimates[i]:.2f}")

print("\nProbabilidades verdadeiras de recompensa:")
for i in range(n_arms):
    print(f"Máquina {i+1}: {true_probs[i]}")
