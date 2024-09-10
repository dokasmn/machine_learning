import numpy as np
import gym

# Criar o ambiente do FrozenLake (4x4)
env = gym.make('FrozenLake-v1', is_slippery=False)

# Configurações do Q-Learning
learning_rate = 0.8      # Taxa de aprendizado (alpha)
discount_factor = 0.95   # Fator de desconto (gamma)
epsilon = 1.0            # Fator de exploração (ε-greedy)
epsilon_decay = 0.99     # Decaimento de epsilon
min_epsilon = 0.01       # Valor mínimo de epsilon
num_episodes = 1000      # Número de episódios para treinamento
max_steps = 100          # Máximo de passos por episódio

# Inicializando a Q-table (tabela Q) com zeros
q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Função de treinamento com Q-Learning
for episode in range(num_episodes):
    # Verifica se o reset() retorna um estado ou uma tupla
    state = env.reset() if isinstance(env.reset(), int) else env.reset()[0]
    done = False

    for step in range(max_steps):
        # Escolher a ação: exploração vs. exploração (ε-greedy)
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Exploração: escolha aleatória
        else:
            action = np.argmax(q_table[state, :])  # Exploração: escolha a melhor ação

        # Executar a ação e receber a nova informação do ambiente
        new_state, reward, done, info, _ = env.step(action)

        # Verifica se o novo estado é um inteiro ou parte de uma tupla
        new_state = new_state if isinstance(new_state, int) else new_state[0]

        # Atualizar a Q-table com a equação do Q-Learning
        q_table[state, action] = q_table[state, action] + learning_rate * (
            reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action]
        )

        # Mudar para o próximo estado
        state = new_state

        # Se o agente cair em um buraco ou atingir o objetivo, termina o episódio
        if done:
            break

    # Decaimento de epsilon para diminuir a exploração ao longo do tempo
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

print("Treinamento concluído!")

# Testando a política treinada
total_rewards = 0
for episode in range(100):
    state = env.reset() if isinstance(env.reset(), int) else env.reset()[0]
    done = False
    step = 0

    while not done:
        # Escolher a ação baseada na Q-table treinada
        action = np.argmax(q_table[state, :])
        new_state, reward, done, info, _ = env.step(action)
        new_state = new_state if isinstance(new_state, int) else new_state[0]
        total_rewards += reward
        state = new_state
        step += 1

        # Descomente para visualizar o agente jogando
        env.render()

print(f"Recompensa total após teste: {total_rewards}")
